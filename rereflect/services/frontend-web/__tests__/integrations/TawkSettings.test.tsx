import { beforeEach, describe, expect, it, vi } from 'vitest';
import { fireEvent, render, screen, waitFor } from '@testing-library/react';
import { TawkSettings } from '@/components/integrations/TawkSettings';

const mock = vi.hoisted(() => ({
  user: { role: 'owner' },
  get: vi.fn(), post: vi.fn(), delete: vi.fn(),
}));
vi.mock('@/contexts/AuthContext', () => ({ useAuth: () => ({ user: mock.user }) }));
vi.mock('@/lib/api-client', () => ({ default: { get: mock.get, post: mock.post, delete: mock.delete } }));
const empty = { connected: false, property_id: null, source_id: null, name: null,
  webhook_url: 'https://api.example.com/api/v1/webhooks/tawk/events', last_event_at: null, events_processed: 0 };
const connected = { ...empty, connected: true, property_id: 'a'.repeat(24), source_id: 7, name: 'Support' };

beforeEach(() => {
  vi.clearAllMocks(); mock.user = { role: 'owner' };
  mock.get.mockResolvedValue({ data: empty });
  mock.post.mockResolvedValue({ data: connected });
  mock.delete.mockResolvedValue({ data: { success: true } });
});

describe('tawk.to configuration', () => {
  it('shows callback and required events, saves property, then clears secret', async () => {
    render(<TawkSettings />);
    expect(await screen.findByLabelText('Property ID')).toBeInTheDocument();
    expect(screen.getByDisplayValue(empty.webhook_url)).toBeInTheDocument();
    expect(screen.getByText(/chat:transcript_created/)).toBeInTheDocument();
    fireEvent.change(screen.getByLabelText('Property ID'), { target: { value: connected.property_id } });
    const secret = screen.getByLabelText('Webhook secret');
    expect(secret).toHaveAttribute('type', 'password');
    fireEvent.change(secret, { target: { value: 'test-signing-secret-123' } });
    fireEvent.click(screen.getByRole('button', { name: 'Save connection' }));
    await waitFor(() => expect(mock.post).toHaveBeenCalledWith('/api/v1/integrations/tawk/connect', {
      property_id: connected.property_id, webhook_secret: 'test-signing-secret-123', name: 'tawk.to support',
    }));
    await waitFor(() => expect(secret).toHaveValue(''));
    expect(screen.getByText('Waiting for first delivery')).toBeInTheDocument();
  });

  it('reports errors without revealing the submitted secret', async () => {
    mock.post.mockRejectedValue({ response: { data: { detail: 'Property is already registered.' } } });
    render(<TawkSettings />);
    fireEvent.change(await screen.findByLabelText('Property ID'), { target: { value: connected.property_id } });
    fireEvent.change(screen.getByLabelText('Webhook secret'), { target: { value: 'test-signing-secret-123' } });
    fireEvent.click(screen.getByRole('button', { name: 'Save connection' }));
    expect(await screen.findByRole('alert')).toHaveTextContent('Property is already registered.');
  });

  it('refreshes observed ingestion and confirms before disconnecting', async () => {
    mock.get.mockResolvedValue({ data: { ...connected, events_processed: 1, last_event_at: '2026-10-07T09:00:00Z' } });
    render(<TawkSettings />);
    expect(await screen.findByText('1 feedback items imported')).toBeInTheDocument();
    fireEvent.click(screen.getByRole('button', { name: 'Refresh status' }));
    await waitFor(() => expect(mock.get).toHaveBeenCalledTimes(2));
    fireEvent.click(screen.getByRole('button', { name: 'Disconnect' }));
    expect(mock.delete).not.toHaveBeenCalled();
    fireEvent.click(screen.getByRole('button', { name: 'Confirm disconnect' }));
    await waitFor(() => expect(mock.delete).toHaveBeenCalledWith('/api/v1/integrations/tawk/disconnect'));
  });

  it('does not expose configuration or fetch credentials to members', async () => {
    mock.user = { role: 'member' };
    render(<TawkSettings />);
    expect(await screen.findByText(/administrator or owner/)).toBeInTheDocument();
    expect(mock.get).not.toHaveBeenCalled();
    expect(screen.queryByLabelText('Webhook secret')).not.toBeInTheDocument();
  });
});
