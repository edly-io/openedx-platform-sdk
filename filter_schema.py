#!/usr/bin/env python3
"""
Filter an OpenAPI schema to only include paths tagged with a specific tag.
Recursively resolves all $ref dependencies so the filtered schema is self-contained.

Usage:
    python filter_schema.py schema.yml filtered_schema.yml openedx-platform-sdk
"""

import sys
import yaml


def collect_refs(obj, refs: set) -> None:
    """Recursively collect all $ref strings from a schema object."""
    if isinstance(obj, dict):
        if "$ref" in obj:
            ref = obj["$ref"]
            # e.g. '#/components/schemas/Xblock' -> 'Xblock'
            if ref.startswith("#/components/schemas/"):
                refs.add(ref.split("/")[-1])
        for v in obj.values():
            collect_refs(v, refs)
    elif isinstance(obj, list):
        for item in obj:
            collect_refs(item, refs)


def resolve_all_refs(names: set, components: dict) -> set:
    """Expand a set of schema names to include all transitive $ref dependencies."""
    resolved = set()
    queue = list(names)
    while queue:
        name = queue.pop()
        if name in resolved:
            continue
        resolved.add(name)
        schema_def = components.get(name)
        if schema_def:
            nested = set()
            collect_refs(schema_def, nested)
            for dep in nested:
                if dep not in resolved:
                    queue.append(dep)
    return resolved


def filter_schema(input_path: str, output_path: str, tag: str) -> None:
    with open(input_path) as f:
        schema = yaml.safe_load(f)

    # 1. Filter paths to only tagged operations
    filtered_paths = {}
    for path, path_item in schema.get("paths", {}).items():
        filtered_methods = {}
        for method, operation in path_item.items():
            if not isinstance(operation, dict):
                continue
            if tag in operation.get("tags", []):
                filtered_methods[method] = operation
        if filtered_methods:
            filtered_paths[path] = filtered_methods

    schema["paths"] = filtered_paths

    # 2. Collect all $refs used directly in filtered paths
    direct_refs: set = set()
    collect_refs(filtered_paths, direct_refs)

    # 3. Recursively resolve transitive dependencies
    all_components = schema.get("components", {}).get("schemas", {})
    all_needed = resolve_all_refs(direct_refs, all_components)

    # 4. Keep only needed components
    if "components" in schema and "schemas" in schema["components"]:
        schema["components"]["schemas"] = {
            k: v for k, v in schema["components"]["schemas"].items()
            if k in all_needed
        }

    with open(output_path, "w") as f:
        yaml.dump(schema, f, allow_unicode=True, sort_keys=False)

    print(f"Filtered schema written to: {output_path}")
    print(f"Paths kept: {len(filtered_paths)}")
    for path in filtered_paths:
        print(f"  {path}")
    print(f"Components kept: {len(all_needed)} (from {len(all_components)} total)")


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print(f"Usage: {sys.argv[0]} <input_schema> <output_schema> <tag>")
        sys.exit(1)
    filter_schema(sys.argv[1], sys.argv[2], sys.argv[3])
