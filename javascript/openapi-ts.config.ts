import { defineConfig } from '@hey-api/openapi-ts';

// Mirrors ../config.yml. Input is the filtered schema produced by
// ../filter_schema.py, so python and js cover the same tagged operations.
export default defineConfig({
  input: '../filtered_schema.yml',
  output: {
    path: 'src/generated',
    format: 'prettier',
  },
  client: '@hey-api/client-axios',
});
