# openedx-platform-sdk

Client libraries for the OpenedX Authoring and Enrollment APIs, auto-generated
from the platform's OpenAPI schema.

| Directory | Package | Generator |
| --- | --- | --- |
| root (`openedx_platform_sdk/`) | `openedx-platform-sdk` (PyPI) | openapi-python-client |
| [`javascript/`](./javascript) | `@openedx/openedx-platform-sdk` (npm) | @hey-api/openapi-ts |

Both are generated from the same filtered schema, so they cover the same
operations. See [`javascript/README.md`](./javascript/README.md) for the JS SDK.

---

A Python client library for the [OpenedX Authoring API](https://docs.openedx.org), auto-generated from the platform's OpenAPI schema using [openapi-python-client](https://github.com/openapi-generators/openapi-python-client).

Covers the standardized v1/v3/v4 Studio APIs and LMS Enrollment v2 APIs tagged `openedx-platform-sdk` in the platform.

---

## Covered APIs

| API | Version | Operations |
|-----|---------|-----------|
| XBlock | v1 | create, retrieve, update, partial_update, destroy |
| Authoring Grading | v3 | partial_update |
| Course Details | v3 | retrieve, update |
| Home | v3 | list, courses, libraries |
| Home (paginated) | v4 | courses |
| Enrollment | v2 | list, retrieve, create, enrollment_allowed, enrollments, roles, course |

---

## Regenerating the SDK

The SDK is generated from the platform's OpenAPI schema. Run this whenever APIs change:

### Prerequisites

```bash
pip install openapi-python-client pyyaml
```

### Steps

Use the provided script — it downloads schemas from both Studio and LMS, merges them, and regenerates the SDK:

```bash
# Regenerate from running Studio + LMS instances
./regen_sdk.sh

# Checkout a specific branch first, then regenerate
# PLATFORM_DIR defaults to ../openedx-platform — override if your checkout is elsewhere
PLATFORM_DIR=/path/to/openedx-platform ./regen_sdk.sh feat/axim-api_improvements

# Use different URLs
STUDIO_URL=http://studio.example.com:8001 LMS_URL=http://lms.example.com:8000 ./regen_sdk.sh
```

---

## Authentication

OpenedX Studio uses JWT tokens via the OAuth2 `client_credentials` flow.

```python
from openedx_platform_sdk import OAuth2ClientCredentials

auth = OAuth2ClientCredentials(
    lms_url="http://local.openedx.io:8000",
    studio_url="http://studio.local.openedx.io:8001/api/contentstore",
    client_id="your-client-id",
    client_secret="your-client-secret",
)

# Studio APIs
with auth.get_studio_client() as client:
    from openedx_platform_sdk.api.openedx_platform_sdk import v3_home_retrieve
    result = v3_home_retrieve.sync(client=client)

# LMS Enrollment APIs
with auth.get_lms_client() as client:
    from openedx_platform_sdk.api.openedx_platform_sdk import v2_enrollment_list
    result = v2_enrollment_list.sync(client=client)
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

with auth.get_studio_client() as client:
    home = v3_home_retrieve.sync(client=client)
    print(home.studio_name)
    print(home.courses)
```

> **Note:** `studio_url` must include `/api/contentstore` — the SDK appends versioned paths (e.g. `/v3/home/`) directly to this base.
>
> Use `auth.get_lms_client()` for Enrollment v2 APIs — it automatically targets `{lms_url}/api/enrollment`.

For typed usage examples covering all API groups (Home v3/v4, Course Details, Authoring Grading, XBlock lifecycle, Enrollment v2), see **[docs/testing-sdk-apis.rst](docs/testing-sdk-apis.rst)**.

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
