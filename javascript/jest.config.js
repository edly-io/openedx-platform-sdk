module.exports = {
  testEnvironment: 'node',
  roots: ['<rootDir>/src'],
  testMatch: ['**/__tests__/**/*.test.ts'],
  transform: {
    '^.+\\.ts$': [
      'ts-jest',
      { tsconfig: { module: 'CommonJS', target: 'ES2020', esModuleInterop: true } },
    ],
  },
  collectCoverageFrom: ['src/**/*.ts', '!src/generated/**', '!src/index.ts'],
};
