import type { Metadata } from 'next';
import IntegrationPage from '@/components/landing/IntegrationPage';

export const metadata: Metadata = {
  title: 'Slack Integration | FeedSignal',
  description:
    'Connect Slack to FeedSignal and turn customer feedback from Slack into sentiment, pain points, and feature requests automatically.',
};

export default function SlackIntegrationPage() {
  return <IntegrationPage slug="slack" />;
}
