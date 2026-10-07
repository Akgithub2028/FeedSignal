import type { ApiKeyScope } from '@/lib/api/api-keys';

export const SCOPE_BADGE_STYLES: Record<string, string> = {
  read: 'bg-blue-100 text-blue-800 dark:bg-blue-900 dark:text-blue-200',
  ingest: 'bg-green-100 text-green-800 dark:bg-green-900 dark:text-green-200',
  write: 'bg-purple-100 text-purple-800 dark:bg-purple-900 dark:text-purple-200',
};

export const SCOPE_DESCRIPTIONS: Record<ApiKeyScope, string> = {
  read: 'Read feedback, customers, and analytics via the public API',
  ingest: 'Submit new feedback and enqueue it for AI analysis',
  write: 'Update existing feedback (status, category/sentiment corrections) via the public API',
};

export function ScopeBadge({ scope }: { scope: string }) {
  const styles = SCOPE_BADGE_STYLES;
  return (
    <span
      className={`inline-flex items-center px-2 py-0.5 rounded text-xs font-medium ${styles[scope] ?? 'bg-gray-100 text-gray-800'}`}
    >
      {scope}
    </span>
  );
}
