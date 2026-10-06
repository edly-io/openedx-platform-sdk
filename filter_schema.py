#!/usr/bin/env python3
"""
Filter an OpenAPI schema to only include paths tagged with a specific tag.
Recursively resolves all $ref dependencies so the filtered schema is self-contained.
Optionally merges a second schema (e.g. LMS enrollment schema) before filtering.

Every path in the output is relative to the service root, so the generated
client takes a bare service URL (``https://studio.example.com``) as its base.
A base schema published with its prefix trimmed has that prefix restored first
(``--base-prefix``, default ``/api/contentstore``).

Usage:
    python filter_schema.py schema.yml filtered_schema.yml openedx-platform-sdk
    python filter_schema.py schema.yml filtered_schema.yml openedx-platform-sdk --merge lms_schema.yml
    python filter_schema.py schema.yml filtered_schema.yml openedx-platform-sdk --base-prefix /api/contentstore
"""

import sys

import yaml


def collect_refs(obj, refs: set) -> None:
    """Recursively collect all $ref strings from a schema object."""
    if isinstance(obj, dict):
        if "$ref" in obj:
            ref = obj["$ref"]
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


DEFAULT_BASE_PREFIX = "/api/contentstore"


def restore_trimmed_prefix(schema: dict, prefix: str) -> None:
    """Prefix every path that was published relative to an API namespace.

    The platform's Studio schema was historically generated with
    ``SCHEMA_PATH_PREFIX_TRIM`` set, so its paths read ``/v1/xblock/`` rather
    than ``/api/contentstore/v1/xblock/`` and consumers had to put the prefix in
    their base URL. The LMS schema, and the Studio schema once the platform
    stops trimming it, publish full paths. Restoring the prefix here gives the
    client one rule for both services, whichever form the platform publishes.

    A path is treated as trimmed when it does not start with ``/api/``. When no
    path is trimmed this is a no-op, and it says so: that is the signal the
    platform has stopped trimming and this step can be deleted.
    """
    paths = schema.get("paths", {})
    trimmed = [path for path in paths if not path.startswith("/api/")]
    if not trimmed:
        print(f"  No trimmed paths in the base schema; '{prefix}' not applied.")
        return
    schema["paths"] = {
        (prefix.rstrip("/") + path if path in trimmed else path): item
        for path, item in paths.items()
    }
    print(f"Restored the trimmed prefix '{prefix}' on {len(trimmed)} base schema path(s).")


def merge_schema(base: dict, extra: dict) -> dict:
    """Merge paths and components from extra into base (base takes precedence on conflict).

    The two schemas come from independent drf-spectacular runs with no shared
    naming discipline, so a name can legitimately mean different things in each.
    Collisions are reported rather than dropped silently: an identical
    definition is harmless, but a differing one means the kept definition now
    describes the discarded one's endpoints too.
    """
    dropped_paths = []
    conflicting_schemas = []
    identical_schemas = []

    for path, path_item in extra.get("paths", {}).items():
        if path not in base.setdefault("paths", {}):
            base["paths"][path] = path_item
        elif base["paths"][path] != path_item:
            dropped_paths.append(path)

    extra_schemas = extra.get("components", {}).get("schemas", {})
    base_schemas = base.setdefault("components", {}).setdefault("schemas", {})
    for name, schema_def in extra_schemas.items():
        if name not in base_schemas:
            base_schemas[name] = schema_def
        elif base_schemas[name] != schema_def:
            conflicting_schemas.append(name)
        else:
            identical_schemas.append(name)

    if dropped_paths:
        print(
            f"WARNING: {len(dropped_paths)} path(s) defined differently in both schemas; "
            "kept the base (CMS) definition:"
        )
        for path in sorted(dropped_paths):
            print(f"  - {path}")

    if conflicting_schemas:
        print(
            f"WARNING: {len(conflicting_schemas)} component schema(s) share a name but differ "
            "between the two services; kept the base (CMS) definition, which now also "
            "describes the LMS endpoints that referenced it:"
        )
        for name in sorted(conflicting_schemas):
            print(f"  - {name}")

    if identical_schemas:
        print(f"  {len(identical_schemas)} component schema(s) defined identically in both; no conflict")

    return base


def fix_path_parameters(paths: dict) -> None:
    """Remove path parameters that are declared but not present in the URL template.

    drf-spectacular emits these on some operations and openapi-python-client
    skips any operation whose declared path parameters don't match its URL.
    They are reported as they are dropped, so a regeneration diff can be traced
    back to the schema rather than looking like an unexplained change.

    Platform schema bug, not a generator bug. Tracked upstream by
    https://github.com/openedx/openedx-platform/issues/39121 — delete this step
    once that is fixed and the committed schemas are regenerated.
    """
    import re
    dropped = []
    for path, path_item in paths.items():
        template_params = set(re.findall(r"\{(\w+)\}", path))
        for method, operation in path_item.items():
            if not isinstance(operation, dict):
                continue
            params = operation.get("parameters", [])
            fixed = [
                p for p in params
                if not (p.get("in") == "path" and p.get("name") not in template_params)
            ]
            if len(fixed) != len(params):
                removed = {p.get("name") for p in params} - {p.get("name") for p in fixed}
                dropped.append((path, method.upper(), sorted(removed)))
                operation["parameters"] = fixed

    if dropped:
        print(
            f"WARNING: dropped {sum(len(names) for _, _, names in dropped)} path parameter(s) "
            "declared on operations whose URL template does not contain them "
            "(a platform schema bug — see "
            "https://github.com/openedx/openedx-platform/issues/39121):"
        )
        for path, method, names in sorted(dropped):
            print(f"  - {method} {path}: {', '.join(names)}")


def filter_schema(
    input_path: str,
    output_path: str,
    tag: str,
    merge_path: str | None = None,
    base_prefix: str = DEFAULT_BASE_PREFIX,
) -> None:
    with open(input_path) as f:
        schema = yaml.safe_load(f)

    restore_trimmed_prefix(schema, base_prefix)

    # Optionally merge a second schema before filtering
    if merge_path:
        with open(merge_path) as f:
            extra_schema = yaml.safe_load(f)
        schema = merge_schema(schema, extra_schema)
        print(f"Merged additional schema from: {merge_path}")

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

    # Fix: remove path parameters declared but absent from the URL template
    # (e.g. /api/enrollment/v2/enrollment/{course_id} incorrectly declares "username" as a path param)
    fix_path_parameters(filtered_paths)

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
    if len(sys.argv) < 4:
        print(
            f"Usage: {sys.argv[0]} <input_schema> <output_schema> <tag> "
            "[--merge <extra_schema>] [--base-prefix <prefix>]"
        )
        sys.exit(1)

    def _option(name: str, default: str | None) -> str | None:
        if name not in sys.argv:
            return default
        idx = sys.argv.index(name)
        if idx + 1 >= len(sys.argv):
            print(f"Error: {name} requires a value", file=sys.stderr)
            sys.exit(1)
        return sys.argv[idx + 1]

    filter_schema(
        sys.argv[1],
        sys.argv[2],
        sys.argv[3],
        merge_path=_option("--merge", None),
        base_prefix=_option("--base-prefix", DEFAULT_BASE_PREFIX),
    )
