'use client';

import type { ChurnSuggestion } from '@/lib/api/churn-suggestions';

// usage_decline evidence is frozen by the backend's `build_evidence` (see
// docs/planning/usage-decline-churn-labels/frontend-settings-and-evidence/spec.md).
// Detect it by shape rather than by the suggestion's `provider` field, since
// EvidenceCell only receives the `evidence` blob.
function isUsageDeclineEvidence(evidence: NonNullable<ChurnSuggestion['evidence']>): boolean {
  return (
    'trend_pct' in evidence ||
    'streak_days' in evidence ||
    'baseline_active_days_14d' in evidence ||
    'current_active_days_14d' in evidence
  );
}

function formatTrendPct(trendPct: unknown): string {
  if (trendPct === null || trendPct === undefined) return 'n/a';
  const n = Number(trendPct);
  if (Number.isNaN(n)) return 'n/a';
  return `${n > 0 ? '+' : ''}${n}%`;
}

function UsageDeclineEvidenceCell({
  evidence,
}: {
  evidence: Record<string, unknown>;
}) {
  const trendPct = formatTrendPct(evidence.trend_pct);
  const baseline = evidence.baseline_active_days_14d as number | undefined;
  const current = evidence.current_active_days_14d as number | undefined;
  const streakDays = evidence.streak_days as number | undefined;
  const lastActiveAt = evidence.last_active_at as string | undefined;

  const activeDaysLine =
    baseline != null && current != null ? `${baseline} → ${current} active days/14d` : null;
  const streakLine = streakDays != null ? `${streakDays}-day streak` : null;
  const lastActiveLine = lastActiveAt
    ? `last active ${new Date(lastActiveAt).toLocaleDateString()}`
    : null;

  return (
    <div className="text-sm">
      <p className="font-medium text-foreground">Usage decline: {trendPct}</p>
      <p className="text-xs text-muted-foreground">
        {[activeDaysLine, streakLine, lastActiveLine].filter(Boolean).join(' · ')}
      </p>
    </div>
  );
}

export function EvidenceCell({ evidence }: { evidence: ChurnSuggestion['evidence'] }) {
  if (!evidence || Object.keys(evidence).length === 0) {
    return <span className="text-sm text-muted-foreground italic">No CRM detail captured</span>;
  }
  if (isUsageDeclineEvidence(evidence)) {
    return <UsageDeclineEvidenceCell evidence={evidence} />;
  }
  const dealName = (evidence.deal_name as string) ?? (evidence.opportunity_name as string);
  const amount = evidence.amount as number | undefined;
  const stage = (evidence.stage as string) ?? (evidence.type as string);
  return (
    <div className="text-sm">
      {dealName && <p className="font-medium text-foreground">{dealName}</p>}
      <p className="text-xs text-muted-foreground">
        {[
          amount != null ? `$${amount.toLocaleString()}` : null,
          stage ?? null,
        ]
          .filter(Boolean)
          .join(' · ')}
      </p>
    </div>
  );
}
