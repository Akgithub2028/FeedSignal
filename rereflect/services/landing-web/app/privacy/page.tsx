import type { Metadata } from 'next';
import LegalPage from '@/components/landing/LegalPage';

export const metadata: Metadata = {
  "title": "Privacy Policy | FeedSignal",
  "description": "How FeedSignal handles website, account and customer feedback data."
};

const sections = [
  {
    "h2": "1. Operator and scope",
    "paragraphs": [
      "FeedSignal is operated by the maintainer of github.com/Akgithub2028/FeedSignal. Contact aayaannkausar@gmail.com for privacy questions. This page describes the FeedSignal website and hosted application. A separately self-hosted installation is controlled by its own operator."
    ]
  },
  {
    "h2": "2. Data used by the application",
    "paragraphs": [
      "The hosted application stores account details, workspace settings, customer feedback and analysis results needed to provide the service. Connected integrations can supply conversation content, customer identifiers and issue information. Connect only workspaces and data you are authorized to use."
    ]
  },
  {
    "h2": "3. Hosting and integrations",
    "paragraphs": [
      "The website and dashboard use Vercel hosting. The backend uses Render and an operator-controlled database. Providers receive the information necessary for their configured features. If a workspace enables an external AI provider, the content submitted for analysis is processed by that provider. Its own terms and privacy policy apply."
    ]
  },
  {
    "h2": "4. Access and security",
    "paragraphs": [
      "The hosted operator can administer the service and its data. Integration credentials are stored using the application encryption settings; access is scoped to workspaces. HTTPS protects traffic in transit. A self-hosted operator is responsible for its infrastructure and configuration."
    ]
  },
  {
    "h2": "5. Browser storage and diagnostics",
    "paragraphs": [
      "The dashboard uses browser storage for sign-in and display preferences. Hosting providers process request metadata and service logs. Optional analytics and error reporting depend on operator configuration."
    ]
  },
  {
    "h2": "6. Export, removal and questions",
    "paragraphs": [
      "Contact aayaannkausar@gmail.com to request help with account data, exports, deletion or integration access. Disconnecting an integration does not automatically delete all previously imported feedback; ask the operator to confirm the intended data removal."
    ]
  },
  {
    "h2": "7. Updates",
    "paragraphs": [
      "Updates to this page are recorded in the FeedSignal repository. Review the date above when checking the current information."
    ]
  }
];

export default function PrivacyPolicyPage() {
  return <LegalPage title="Privacy Policy" updated="October 6, 2026" sections={sections} />;
}
