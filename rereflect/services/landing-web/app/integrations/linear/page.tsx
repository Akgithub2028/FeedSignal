import type { Metadata } from 'next';
import IntegrationPage from '@/components/landing/IntegrationPage';

export const metadata: Metadata = {
  title: 'Linear Integration | FeedSignal',
  description:
    'Connect Linear to FeedSignal and turn customer feedback from Linear into sentiment, pain points, and feature requests automatically.',
};

export default function LinearIntegrationPage() {
  return <IntegrationPage slug="linear" />;
}
