import type { Metadata } from 'next';
import IntegrationPage from '@/components/landing/IntegrationPage';

export const metadata: Metadata = {
  title: 'Jira Integration | FeedSignal',
  description:
    'Connect Jira to FeedSignal and turn customer feedback from Jira into sentiment, pain points, and feature requests automatically.',
};

export default function JiraIntegrationPage() {
  return <IntegrationPage slug="jira" />;
}
