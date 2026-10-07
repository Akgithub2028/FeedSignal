import { describe, it, expect, vi } from 'vitest';
vi.mock('next/navigation', () => ({ notFound: () => { throw new Error('NEXT_NOT_FOUND'); } }));
import RetiredPage from '../page';
describe('retired provider route', () => {
  it('returns not-found rather than an active connection screen', () => {
    expect(() => RetiredPage()).toThrow('NEXT_NOT_FOUND');
  });
});
