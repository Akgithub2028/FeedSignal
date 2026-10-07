import type { Metadata } from 'next';
import LegalPage from '@/components/landing/LegalPage';

export const metadata: Metadata = {
  "title": "Terms of Service | FeedSignal",
  "description": "Terms for the FeedSignal website, hosted service and open-source software."
};

const sections = [
  {
    "h2": "1. Service and operator",
    "paragraphs": [
      "FeedSignal provides customer feedback analysis and connected workspace tools. It is operated by the maintainer of github.com/Akgithub2028/FeedSignal. Contact aayaannkausar@gmail.com for service questions."
    ]
  },
  {
    "h2": "2. Software license and attribution",
    "paragraphs": [
      "FeedSignal is derived from Rereflect (github.com/haqaliz/rereflect). The source code is distributed under the MIT License included in the repository. Original copyright and permission notices remain applicable. This fork is maintained independently of the upstream project."
    ]
  },
  {
    "h2": "3. Accounts and connected data",
    "paragraphs": [
      "Use only accounts, workspaces and data you are authorized to access. Protect your credentials and review the permissions granted to integrations. You retain responsibility for the customer data you submit and the messages or issue updates you choose to send."
    ]
  },
  {
    "h2": "4. Hosting and provider costs",
    "paragraphs": [
      "Open-source licensing and the operation of a hosted service are separate. Hosting, email and AI providers can have their own charges and limits. Review any applicable plan before enabling a paid provider feature."
    ]
  },
  {
    "h2": "5. Analysis and availability",
    "paragraphs": [
      "AI-generated classifications, summaries and suggestions can be incorrect. Review results before using them to make decisions or contact customers. Availability also depends on hosting and connected providers; interrupted integrations can delay ingestion or scheduled work."
    ]
  },
  {
    "h2": "6. Self-hosted installations",
    "paragraphs": [
      "If you operate your own installation, you control its database, hosting, credentials and retention settings. Maintain backups, access controls and provider configuration for that installation."
    ]
  },
  {
    "h2": "7. Contact and updates",
    "paragraphs": [
      "Contact aayaannkausar@gmail.com for support or questions. Updates to these pages are recorded in the FeedSignal repository. The MIT License text in the repository governs the software license."
    ]
  }
];

export default function TermsPage() {
  return <LegalPage title="Terms of Service" updated="October 6, 2026" sections={sections} />;
}
