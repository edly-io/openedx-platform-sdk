# openedx-platform-sdk

A Python client library for the [OpenedX Authoring API](https://docs.openedx.org), auto-generated from the platform's OpenAPI schema using [openapi-python-client](https://github.com/openapi-generators/openapi-python-client).

Covers the standardized v1/v3/v4 APIs tagged `openedx-platform-sdk` in the platform.

---

## Covered APIs

| API | Version | Operations |
|-----|---------|-----------|
| XBlock | v1 | create, retrieve, update, partial_update, destroy |
| Authoring Grading | v3 | partial_update |
| Course Details | v3 | retrieve, update |
| Home | v3 | list, courses, libraries |
| Home (paginated) | v4 | courses |

---

## Regenerating the SDK

The SDK is generated from the platform's OpenAPI schema. Run this whenever APIs change:

### Prerequisites

```bash
pip install openapi-python-client pyyaml
```

### Steps

```bash
# 1. Download the schema from a running Studio instance
curl http://studio.local.openedx.io:8001/authoring-api/schema/ > schema.yml

# 2. Filter schema to only openedx-platform-sdk tagged paths
python filter_schema.py schema.yml filtered_schema.yml openedx-platform-sdk

# 3. Regenerate the SDK
openapi-python-client generate \
  --path filtered_schema.yml \
  --config config.yml
```

Or use the provided script (supports optional branch checkout):

```bash
./regen_sdk.sh                              # uses current platform branch
./regen_sdk.sh feat/axim-api_improvements   # checkout branch first, then regenerate
```

---

## Authentication

OpenedX Studio uses JWT tokens via the OAuth2 `client_credentials` flow.

```python
from openedx_platform_sdk import OAuth2ClientCredentials

auth = OAuth2ClientCredentials(
    lms_url="http://localhost:18000",
    client_id="your-client-id",
    client_secret="your-client-secret",
)

# Get a ready-to-use authenticated client (token fetched automatically)
with auth.get_client(studio_url="http://localhost:18010/api/contentstore") as client:
    from openedx_platform_sdk.api.openedx_platform_sdk import v3_home_list
    result = v3_home_list.sync(client=client)
```

Token is cached and auto-refreshed 60 seconds before expiry. The `JWT` prefix is used automatically (required by OpenedX).

---

## Usage

### Basic authenticated client

```python
from openedx_platform_sdk import AuthenticatedClient

client = AuthenticatedClient(
    base_url="http://localhost:18010/api/contentstore",
    token="your-jwt-token",
    prefix="JWT",
)
```

### Call an endpoint

```python
from openedx_platform_sdk.api.openedx_platform_sdk import v3_home_list
from openedx_platform_sdk.api.openedx_platform_sdk import v3_course_details_retrieve
from openedx_platform_sdk.api.openedx_platform_sdk import v4_home_courses_list

with client as client:
    # Get studio home
    home = v3_home_list.sync(client=client)

    # Get course details
    details = v3_course_details_retrieve.sync(
        client=client,
        course_id="course-v1:org+course+run",
    )

    # Get paginated courses (v4)
    courses = v4_home_courses_list.sync(client=client, page=1, page_size=20)
```

### Async support

```python
import asyncio
from openedx_platform_sdk.api.openedx_platform_sdk import v3_home_list

async def main():
    async with client as c:
        home = await v3_home_list.asyncio(client=c)

asyncio.run(main())
```

### Detailed response (status code, headers)

```python
from openedx_platform_sdk.api.openedx_platform_sdk import v3_home_list
from openedx_platform_sdk.types import Response

with client as client:
    response: Response = v3_home_list.sync_detailed(client=client)
    print(response.status_code)
    print(response.parsed)
```

---

## Installation

```bash
# From source
pip install .

# With Poetry
poetry install
```

---

## Publishing

```bash
poetry publish --build
```
