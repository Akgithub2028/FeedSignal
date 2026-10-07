import type { Metadata } from 'next';
import IntegrationPage from '@/components/landing/IntegrationPage';

export const metadata: Metadata = {
  title: 'Asana Integration | FeedSignal',
  description:
    'Connect Asana to FeedSignal and turn customer feedback from Asana into sentiment, pain points, and feature requests automatically.',
};

export default function AsanaIntegrationPage() {
  return <IntegrationPage slug="asana" />;
}
