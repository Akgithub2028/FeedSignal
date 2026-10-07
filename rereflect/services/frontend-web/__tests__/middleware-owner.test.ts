import { afterEach, describe, expect, it, vi } from 'vitest';
import { NextRequest } from 'next/server';

afterEach(() => { vi.unstubAllEnvs(); vi.resetModules(); });

describe('owner marketing redirects', () => {
  it('redirects legal pages to the configured owner origin and retains the query', async () => {
    vi.stubEnv('MARKETING_URL', 'https://landing.example.com');
    const { middleware } = await import('../middleware');
    const response = middleware(new NextRequest('https://app.example.com/privacy?lang=en'));
    expect(response.headers.get('location')).toBe('https://landing.example.com/privacy?lang=en');
  });

  it('does not send a similarly prefixed dashboard path to marketing', async () => {
    vi.stubEnv('MARKETING_URL', 'https://landing.example.com');
    const { middleware } = await import('../middleware');
    const response = middleware(new NextRequest('https://app.example.com/privacy-settings'));
    expect(response.headers.get('location')).toBeNull();
  });
});
