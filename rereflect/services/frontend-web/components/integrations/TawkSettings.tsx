'use client';

import { useCallback, useEffect, useState } from 'react';
import Link from 'next/link';
import { useAuth } from '@/contexts/AuthContext';
import apiClient from '@/lib/api-client';
import { Button } from '@/components/ui/button';
import { Input } from '@/components/ui/input';
import { Label } from '@/components/ui/label';
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card';

interface Connection {
  connected: boolean;
  property_id: string | null;
  source_id: number | null;
  name: string | null;
  webhook_url: string | null;
  last_event_at: string | null;
  events_processed: number;
}

function errorMessage(error: unknown): string {
  const detail = (error as { response?: { data?: { detail?: unknown } } })?.response?.data?.detail;
  return typeof detail === 'string' ? detail : 'Could not save tawk.to settings. Please try again.';
}

export function TawkSettings() {
  const { user } = useAuth();
  const allowed = user?.role === 'owner' || user?.role === 'admin';
  const [status, setStatus] = useState<Connection | null>(null);
  const [property, setProperty] = useState('');
  const [name, setName] = useState('tawk.to support');
  const [secret, setSecret] = useState('');
  const [error, setError] = useState<string | null>(null);
  const [busy, setBusy] = useState(false);
  const [confirmDisconnect, setConfirmDisconnect] = useState(false);

  const refresh = useCallback(async () => {
    if (!allowed) return;
    setError(null);
    try {
      const { data } = await apiClient.get<Connection>('/api/v1/integrations/tawk/status');
      setStatus(data);
      setProperty(data.property_id || '');
      setName(data.name || 'tawk.to support');
    } catch {
      setError('Could not load tawk.to settings. Refresh to try again.');
    }
  }, [allowed]);
  useEffect(() => { void refresh(); }, [refresh]);

  if (!user) return <p>Loading…</p>;
  if (!allowed) return <p>You must be an administrator or owner to configure tawk.to.</p>;

  async function save(event: React.FormEvent) {
    event.preventDefault();
    setBusy(true); setError(null);
    try {
      const { data } = await apiClient.post<Connection>('/api/v1/integrations/tawk/connect', {
        property_id: property.trim(), webhook_secret: secret, name: name.trim(),
      });
      setStatus(data);
      setSecret('');
    } catch (err) {
      setError(errorMessage(err));
    } finally { setBusy(false); }
  }

  async function disconnect() {
    setBusy(true); setError(null);
    try {
      await apiClient.delete('/api/v1/integrations/tawk/disconnect');
      setStatus(previous => previous ? { ...previous, connected: false } : null);
      setSecret('');
      setConfirmDisconnect(false);
    } catch (err) { setError(errorMessage(err)); }
    finally { setBusy(false); }
  }

  return <div className="space-y-6 max-w-3xl">
    <Link href="/settings/integrations" className="text-sm text-muted-foreground">← Integrations</Link>
    <h1 className="text-2xl font-semibold">tawk.to support feedback</h1>
    <p className="text-muted-foreground">Import visitor messages from completed chats and newly created support tickets. Agent replies and system messages are excluded. Replies and ticket updates are not synchronized.</p>
    {error && <p role="alert" className="text-destructive">{error}</p>}
    <Card>
      <CardHeader><CardTitle>Connect your property</CardTitle></CardHeader>
      <CardContent className="space-y-4">
        <ol className="list-decimal pl-5 space-y-2 text-sm">
          <li>Open your property in <a href="https://dashboard.tawk.to/" target="_blank" rel="noopener noreferrer" className="underline">tawk.to</a>, then Administration → Settings → Webhooks.</li>
          <li>Create a webhook using the callback below. Enable <code>chat:transcript_created</code> and <code>ticket:create</code>.</li>
          <li>Copy its property ID and webhook secret into this form. Send a test chat or ticket, then refresh status.</li>
        </ol>
        <Label htmlFor="tawk-callback">Webhook callback URL</Label>
        <Input id="tawk-callback" value={status?.webhook_url || ''} readOnly />
        {!status?.webhook_url && status && <p className="text-sm text-destructive">The operator must configure the backend public URL before connecting.</p>}
        <form onSubmit={save} className="space-y-4">
          <div><Label htmlFor="tawk-name">Source name</Label><Input id="tawk-name" value={name} onChange={e => setName(e.target.value)} required maxLength={255} /></div>
          <div><Label htmlFor="tawk-property">Property ID</Label><Input id="tawk-property" value={property} onChange={e => setProperty(e.target.value)} required pattern="[a-f0-9]{24}" placeholder="24-character property ID" /></div>
          <div><Label htmlFor="tawk-secret">Webhook secret</Label><Input id="tawk-secret" type="password" value={secret} onChange={e => setSecret(e.target.value)} autoComplete="new-password" required minLength={16} maxLength={512} />
            <p className="text-xs text-muted-foreground mt-1">Stored encrypted and never returned. Enter the secret again to update or reconnect.</p></div>
          <Button type="submit" disabled={busy || !status?.webhook_url}>{busy ? 'Saving…' : 'Save connection'}</Button>
        </form>
      </CardContent>
    </Card>
    {status && <Card>
      <CardHeader><CardTitle>Delivery status</CardTitle></CardHeader>
      <CardContent className="space-y-3">
        <p>{status.connected ? 'Connection configured' : 'Disconnected'}</p>
        <p>{status.last_event_at ? `Last signed delivery: ${new Date(status.last_event_at).toLocaleString()}` : 'Waiting for first delivery'}</p>
        <p>{status.events_processed} feedback items imported</p>
        <p className="text-sm text-muted-foreground">Imported feedback is saved immediately. AI analysis runs when background processing is available.</p>
        {status.source_id && <Link href={`/feedback-sources/${status.source_id}`} className="underline text-sm">View source and delivery receipts</Link>}
        <div className="flex gap-2"><Button variant="outline" onClick={() => void refresh()} disabled={busy}>Refresh status</Button>
          {status.connected && <Button variant="destructive" onClick={() => setConfirmDisconnect(true)} disabled={busy}>Disconnect</Button>}</div>
        {confirmDisconnect && <div role="alertdialog" aria-label="Disconnect tawk.to" className="border rounded-lg p-4 space-y-3">
          <p>Stop new ingestion? Existing feedback and delivery history will be preserved. Remove the webhook in tawk.to too.</p>
          <Button variant="destructive" onClick={() => void disconnect()} disabled={busy}>Confirm disconnect</Button>
          <Button variant="outline" onClick={() => setConfirmDisconnect(false)}>Cancel</Button>
        </div>}
      </CardContent>
    </Card>}
  </div>;
}
