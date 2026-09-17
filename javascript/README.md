# openedx-platform-sdk (JavaScript)

A TypeScript client library for the OpenedX Authoring and Enrollment APIs,
auto-generated from the platform's OpenAPI schema using
[@hey-api/openapi-ts](https://github.com/hey-api/openapi-ts).

Generated from the same filtered schema as the Python SDK, so both cover the
operations tagged `openedx-platform-sdk` in the platform.

## Install

```bash
npm install @openedx/openedx-platform-sdk
```

## Usage

```ts
import { OAuth2ClientCredentials, v4HomeCoursesRetrieve } from '@openedx/openedx-platform-sdk';

const auth = new OAuth2ClientCredentials({
  lmsUrl: 'http://local.openedx.io:8000',
  studioUrl: 'http://studio.local.openedx.io:8001/api/contentstore',
  clientId: 'your-client-id',
  clientSecret: 'your-client-secret',
});

const client = await auth.getStudioClient();
const { data } = await v4HomeCoursesRetrieve({ client });

const lmsClient = await auth.getLmsClient();
```

Tokens are fetched with the OAuth2 `client_credentials` grant, sent with the
`JWT` prefix that OpenedX expects, and refreshed automatically before expiry.

### Use inside an MFE

MFEs already hold an authenticated session, so skip `OAuth2ClientCredentials`
and build a client around the existing axios instance:

```ts
import { createClient } from '@hey-api/client-axios';
import { getAuthenticatedHttpClient } from '@edx/frontend-platform/auth';

const client = createClient({ axios: getAuthenticatedHttpClient(), baseURL: studioUrl });
```

## Regenerating

`src/generated/` is produced by the generator and committed, matching how the
Python package is handled. `src/auth.ts` and `src/index.ts` are hand-written and
are never touched by the generator.

### Prerequisites

```bash
pip install pyyaml
cd javascript && npm install
```

### Steps

From the repo root, using the same schema sources as `regen_sdk.sh`:

```bash
# From running Studio + LMS instances
STUDIO_URL=http://studio.local.openedx.io:8001 \
LMS_URL=http://local.openedx.io:8000 \
./regen_sdk_js.sh

# From a local platform checkout
PLATFORM_DIR=/path/to/openedx-platform ./regen_sdk_js.sh

# From schema files (used by CI)
CMS_SCHEMA_FILE=platform/cms_schema.yml \
LMS_SCHEMA_FILE=platform/lms_schema.yml \
./regen_sdk_js.sh
```

The weekly `regenerate_sdk.yml` workflow regenerates both SDKs and opens a PR.

## Development

```bash
npm run validate   # lint, typecheck and test
npm run build      # dual CJS/ESM build with type declarations
```

`typecheck` and `build` require `src/generated/` to exist, so run the
regeneration script first on a fresh checkout.
