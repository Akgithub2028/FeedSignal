import { afterEach, beforeEach, describe, expect, it, vi } from 'vitest';
import path from 'path';

const wrap = vi.hoisted(() => vi.fn((config, options) => ({ ...config, sentryOptions: options })));
vi.mock('@sentry/nextjs', () => ({ withSentryConfig: wrap }));
beforeEach(() => {
  for (const name of ['SENTRY_DSN', 'NEXT_PUBLIC_SENTRY_DSN', 'SENTRY_ORG', 'SENTRY_PROJECT', 'SENTRY_AUTH_TOKEN']) vi.stubEnv(name, '');
  vi.stubEnv('VERCEL', '');
  wrap.mockClear();
});
afterEach(() => { vi.unstubAllEnvs(); vi.resetModules(); });

describe('operator Sentry configuration', () => {
  it('uses Vercel packaging instead of the Docker standalone output on Vercel', async () => {
    vi.stubEnv('VERCEL', '1');
    const { default: config } = await import('../next.config');
    expect(config.output).toBeUndefined();
  });
  it('lets the Vercel builder resolve the app from the Git repository root', async () => {
    vi.stubEnv('VERCEL', '1');
    const { default: config } = await import('../next.config');
    const relativeAppDir = path.relative(config.outputFileTracingRoot as string, path.resolve(import.meta.dirname, '..'));
    expect(relativeAppDir).toBe(path.join('rereflect', 'services', 'frontend-web'));
  });
  it('leaves telemetry tooling disabled when no operator configuration exists', async () => {
    const { default: config } = await import('../next.config');
    expect(config.output).toBe('standalone');
    expect(wrap).not.toHaveBeenCalled();
  });
  it('uses the owner project and permits uploads only with complete owner settings', async () => {
    vi.stubEnv('SENTRY_ORG', 'owner-org');
    vi.stubEnv('SENTRY_PROJECT', 'feedsignal');
    vi.stubEnv('SENTRY_AUTH_TOKEN', 'test-only-token');
    await import('../next.config');
    expect(wrap).toHaveBeenCalledWith(expect.anything(), expect.objectContaining({
      org: 'owner-org', project: 'feedsignal', sourcemaps: { disable: false },
    }));
  });
});
