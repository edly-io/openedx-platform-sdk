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

Or use the provided script:

```bash
# Regenerate from a running Studio (no platform repo needed)
./regen_sdk.sh

# Checkout a specific branch first, then regenerate
# PLATFORM_DIR defaults to ../openedx-platform — override if your checkout is elsewhere
PLATFORM_DIR=/path/to/openedx-platform ./regen_sdk.sh feat/axim-api_improvements

# Use a different Studio URL
STUDIO_URL=http://studio.example.com:8001 ./regen_sdk.sh
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
with auth.get_client(studio_url="http://studio.local.openedx.io:8001/api/contentstore") as client:
    from openedx_platform_sdk.api.openedx_platform_sdk import v3_home_retrieve
    result = v3_home_retrieve.sync(client=client)
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
from openedx_platform_sdk.api.openedx_platform_sdk import v3_home_retrieve
from openedx_platform_sdk.api.openedx_platform_sdk import v3_course_details_retrieve
from openedx_platform_sdk.api.openedx_platform_sdk import v4_home_courses_retrieve

with client as client:
    # Get studio home
    home = v3_home_retrieve.sync(client=client)

    # Get course details
    details = v3_course_details_retrieve.sync(
        client=client,
        course_id="course-v1:org+course+run",
    )

    # Get paginated courses (v4)
    courses = v4_home_courses_retrieve.sync(client=client)
```

### Async support

```python
import asyncio
from openedx_platform_sdk.api.openedx_platform_sdk import v3_home_retrieve

async def main():
    async with client as c:
        home = await v3_home_retrieve.asyncio(client=c)

asyncio.run(main())
```

### Detailed response (status code, headers)

```python
from openedx_platform_sdk.api.openedx_platform_sdk import v3_home_retrieve
from openedx_platform_sdk.types import Response

with client as client:
    response: Response = v3_home_retrieve.sync_detailed(client=client)
    print(response.status_code)
    print(response.parsed)
```

---

## Testing Locally

### Prerequisites

- A running [devstack](https://github.com/openedx/devstack) or Tutor instance
- Default URLs: LMS at `http://local.openedx.io:8000`, Studio at `http://studio.local.openedx.io:8001`

### 1. Install the SDK

```bash
cd openedx-platform-sdk
pip install -e .
```

### 2. Create an OAuth2 application in LMS

1. Go to `http://local.openedx.io:8000/admin/oauth2_provider/application/`
2. Click **Add Application**
3. Fill in:
   - **User**: any staff/admin user (required for JWT issuance)
   - **Client type**: Confidential
   - **Authorization grant type**: Client credentials
   - **Name**: `openedx-platform-sdk`
4. Save and copy the generated **Client ID** and **Client Secret**

### 3. Run a quick test

```python
from openedx_platform_sdk import OAuth2ClientCredentials
from openedx_platform_sdk.api.openedx_platform_sdk import v3_home_retrieve

auth = OAuth2ClientCredentials(
    lms_url="http://local.openedx.io:8000",
    client_id="your-client-id",
    client_secret="your-client-secret",
)

with auth.get_client(studio_url="http://studio.local.openedx.io:8001/api/contentstore") as client:
    home = v3_home_retrieve.sync(client=client)
    print(home.studio_name)
    print(home.courses)
```

> **Note:** The `studio_url` must include `/api/contentstore` — the SDK appends versioned paths (e.g. `/v3/home/`) directly to this base.

For typed usage examples covering all API groups (Home v3/v4, Course Details, Authoring Grading, XBlock lifecycle), see **[docs/testing-sdk-apis.rst](docs/testing-sdk-apis.rst)**.

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
