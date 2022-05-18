module.exports = {
  testRunner: 'jasmine2',
  testEnvironment: 'node',
  // moduleFileExtensions: ['js', 'json', 'jsx', 'ts', 'tsx', 'node'],
  setupFilesAfterEnv: ['jest-allure/dist/setup'],
  moduleFileExtensions: ['js', 'json', 'ts'],
  rootDir: '.',
  testRegex: '.e2e-spec.ts$',
  transform: {
    '^.+\\.(t|j)s$': 'ts-jest',
  },
};
