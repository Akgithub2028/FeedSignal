export interface IntegrationStep {
  step: string;
  title: string;
  description: string;
}

export interface IntegrationFeature {
  title: string;
  description: string;
  icon: string; // lucide-react icon name
}

export interface IntegrationUseCase {
  persona: string;
  role: string;
  quote: string;
  icon: string; // lucide-react icon name
}

export interface IntegrationFAQ {
  question: string;
  answer: string;
}

export interface IntegrationSetupStep {
  step: number;
  title: string;
  description: string;
}

export interface Integration {
  slug: string;
  name: string;
  tagline: string;
  description: string;
  status: 'available' | 'coming_soon';
  color: string;
  gradient: string;
  hoverShadow: string;
  hoverBorder: string;
  heroMessage: string;
  howItWorks: IntegrationStep[];
  features: IntegrationFeature[];
  useCases: IntegrationUseCase[];
  faqs: IntegrationFAQ[];
  setupSteps: IntegrationSetupStep[];
}

const SHARED_FAQS: IntegrationFAQ[] = [
  {
    question: 'How long does setup take?',
    answer: 'Usually a couple of minutes. Connect the integration, choose which channels or conversations to monitor, and FeedSignal starts analyzing feedback immediately.',
  },
  {
    question: 'Is my data secure?',
    answer: 'FeedSignal is self-hosted — it runs on your own infrastructure, so your data never leaves it. Connection credentials are encrypted at rest, and FeedSignal only reads the data you authorize.',
  },
  {
    question: 'Which plan includes integrations?',
    answer: 'All of them. FeedSignal is open-source and self-hosted, so every integration is included with no plans, seats, or paywalls — you run it on your own infrastructure.',
  },
  {
    question: 'Can I use multiple integrations at once?',
    answer: 'Yes. Connect as many sources as you need — Slack, tawk.to, email, and CSV all feed into the same dashboard, and FeedSignal automatically deduplicates and categorizes everything. HubSpot provides optional CRM enrichment.',
  },
  {
    question: 'What if I need an integration you don\'t support yet?',
    answer: 'Because FeedSignal is open-source, you can build it yourself or request it on GitHub. You can also use the webhook API to connect any tool that can send an HTTP request.',
  },
];

const JIRA_FAQS: IntegrationFAQ[] = [
  ...SHARED_FAQS,
  {
    question: 'Does this support Jira Server, Data Center, or OAuth?',
    answer: 'This release supports Jira Cloud only — any *.atlassian.net site, connected with a personal Atlassian API token. Jira Server, Data Center, and native OAuth (3LO) app installation are planned for a future release.',
  },
];



const ASANA_FAQS: IntegrationFAQ[] = [
  ...SHARED_FAQS,
  {
    question: 'Does this sync tasks back into FeedSignal, or use OAuth?',
    answer: 'This is one-way, outbound task creation — FeedSignal creates Asana tasks from feedback, it doesn\'t pull task status or comments back in. Connection uses a personal Asana access token, not OAuth. The workspace/project picker is flat, so team-only projects that aren\'t visible at the workspace level may not appear; a team-scoped picker is planned for a future release.',
  },
];

export const integrations: Integration[] = [
  {
    slug: 'slack',
    name: 'Slack',
    tagline: 'Capture customer feedback from Slack channels automatically',
    description: 'Connect your Slack workspace and let FeedSignal monitor customer-facing channels for feedback, feature requests, and pain points — all analyzed by AI in real-time.',
    status: 'available',
    color: 'chart-4',
    gradient: 'from-[#4A154B] to-[#36C5F0]',
    hoverShadow: 'hover:shadow-[#4A154B]/10',
    hoverBorder: 'hover:border-[#4A154B]/30',
    heroMessage: 'Stop losing feedback in Slack threads. FeedSignal automatically detects customer sentiment, flags urgent issues, and routes feedback to the right team members — all from your existing Slack channels.',
    howItWorks: [
      { step: '1', title: 'Connect Slack', description: 'Authorize FeedSignal with one click. Choose which channels to monitor for customer feedback.' },
      { step: '2', title: 'AI Analyzes Messages', description: 'Our AI reads new messages in real-time, detecting sentiment, pain points, feature requests, and churn risk.' },
      { step: '3', title: 'Get Actionable Insights', description: 'View categorized feedback on your dashboard. Get alerts for urgent issues. Export reports for stakeholders.' },
    ],
    features: [
      { title: 'Channel Monitoring', description: 'Select specific Slack channels to monitor. FeedSignal only reads channels you authorize — nothing else.', icon: 'Hash' },
      { title: 'Real-Time Analysis', description: 'Every message is analyzed as it arrives. No batch processing, no delays — instant sentiment detection.', icon: 'Zap' },
      { title: 'Urgent Alerts', description: 'Get notified immediately when a customer expresses frustration or churn risk. Respond before it escalates.', icon: 'Bell' },
      { title: 'Keyword Triggers', description: 'Set up custom keywords to filter which messages are captured as feedback. Focus on what matters.', icon: 'Search' },
      { title: 'Slack Notifications', description: 'Receive AI-generated alerts back in Slack when anomalies are detected — sentiment spikes, volume changes, and more.', icon: 'MessageSquare' },
      { title: 'Auto-Categorization', description: 'AI automatically tags feedback as bug reports, feature requests, praise, or complaints. No manual sorting.', icon: 'Tags' },
    ],
    useCases: [
      { persona: 'SaaS Founder', role: 'Early-stage, 10-person team', quote: 'Our support channel was a goldmine of feedback we were ignoring. Now FeedSignal surfaces the top pain points every week — we shipped 3 fixes last month based on Slack feedback alone.', icon: 'Rocket' },
      { persona: 'Community Manager', role: 'Developer tools company', quote: 'I manage 5 Slack communities with 2,000+ members. FeedSignal catches the feature requests I used to miss and shows me sentiment trends I never could have tracked manually.', icon: 'Users' },
      { persona: 'Product Manager', role: 'B2B SaaS, 50K users', quote: 'Instead of scrolling through Slack all day, I check FeedSignal\'s dashboard once in the morning. The AI-generated insights are better than what I used to produce from hours of manual review.', icon: 'Layers' },
    ],
    faqs: SHARED_FAQS,
    setupSteps: [
      { step: 1, title: 'Go to Settings → Integrations', description: 'Navigate to your FeedSignal dashboard and open the Integrations page.' },
      { step: 2, title: 'Click "Connect Slack"', description: 'You\'ll be redirected to Slack to authorize FeedSignal. Choose the workspace you want to connect.' },
      { step: 3, title: 'Select channels to monitor', description: 'Pick which Slack channels contain customer feedback. You can add or remove channels anytime.' },
      { step: 4, title: 'Set up feedback triggers', description: 'Optionally configure keywords or message filters to focus on specific types of feedback.' },
      { step: 5, title: 'Start receiving insights', description: 'That\'s it! Feedback will appear in your dashboard within minutes as messages come in.' },
    ],
  },
  {
    slug: 'teams',
    name: 'Microsoft Teams',
    tagline: 'Get feedback alerts delivered to your Microsoft Teams channels',
    description: 'Connect a Teams webhook and let FeedSignal post alerts — urgent feedback, health drops, sentiment spikes, automation and playbook notifications — straight to the Teams channel where your team works.',
    status: 'available',
    color: 'chart-4',
    gradient: 'from-[#6264A7] to-[#8B8CC7]',
    hoverShadow: 'hover:shadow-[#6264A7]/10',
    hoverBorder: 'hover:border-[#6264A7]/30',
    heroMessage: 'Your team already lives in Teams. FeedSignal meets you there: connect a webhook once, and alerts about urgent feedback, customer health drops, sentiment spikes and churn risk land in the channel your team actually watches.',
    howItWorks: [
      { step: '1', title: 'Create an Incoming Webhook in Teams', description: 'In a Teams channel, use the Incoming Webhook connector (or a Power Automate Workflows URL) to get a webhook URL. No OAuth app to register — the URL is the credential.' },
      { step: '2', title: 'Paste the URL into FeedSignal', description: 'Settings → Integrations → Microsoft Teams. FeedSignal validates the URL and sends a test message to confirm the channel receives it.' },
      { step: '3', title: 'Alerts arrive as cards', description: 'Urgent feedback, health-drop and recovery alerts, automation notifications and playbook notify steps post to Teams as formatted message cards — each team member can toggle Teams on or off per alert type.' },
    ],
    features: [
      { title: 'Urgent Feedback Alerts', description: 'Get an alert the moment feedback is flagged urgent or a churn risk is detected — right in the channel your team watches.', icon: 'Bell' },
      { title: 'Health-Drop Alerts', description: 'Customer health drops and recoveries are posted to Teams, once per organization, when any team member has the alert type enabled.', icon: 'Activity' },
      { title: 'Automation Notifications', description: 'The automation `send_notification` action supports Teams as a destination channel — rules created with `channels: ["teams"]` post there when they fire.', icon: 'Workflow' },
      { title: 'Playbook Notify Steps', description: 'The playbook `notify` action can target Teams from the playbook editor, alongside Slack and Discord.', icon: 'BookOpen' },
      { title: 'Per-User Channel Toggle', description: 'Each team member controls their own Teams delivery per alert type from Settings → Notifications — defaulting to on.', icon: 'Settings2' },
      { title: 'MessageCard Formatting', description: 'Alerts render as Microsoft MessageCards with FeedSignal\u2019s accent color — the format Teams webhooks accept natively.', icon: 'MessageSquare' },
    ],
    useCases: [
      { persona: 'SaaS Founder', role: 'Early-stage, small team', quote: 'We live in Teams. Now urgent feedback and churn signals land in our #customer-alerts channel without anyone having to check another dashboard.', icon: 'Rocket' },
      { persona: 'Customer Success Manager', role: 'B2B SaaS', quote: 'The health-drop alert hits Teams the moment a key account slips. I catch at-risk customers hours earlier than I did with the daily email digest.', icon: 'Heart' },
      { persona: 'Support Lead', role: 'Mid-market SaaS', quote: 'Support tickets flagged urgent now appear as cards in our #support-ops channel, so the right person sees them without a notification hunt.', icon: 'Headphones' },
    ],
    faqs: SHARED_FAQS,
    setupSteps: [
      { step: 1, title: 'Create an Incoming Webhook in Teams', description: 'In your Teams channel, go to the "..." menu → Connectors → Incoming Webhook, name it (e.g. "FeedSignal Alerts"), and copy the webhook URL. Power Automate "Post to a channel when a webhook request is received" Workflows URLs work too.' },
      { step: 2, title: 'Go to Settings → Integrations', description: 'Navigate to your FeedSignal dashboard and open Settings → Integrations → Microsoft Teams.' },
      { step: 3, title: 'Paste the webhook URL', description: 'Paste the URL and click Connect. FeedSignal validates the format (classic `outlook.office.com/webhook/…` or `webhook.office.com/webhookb2/…` Workflows URLs) and rejects invalid ones on save.' },
      { step: 4, title: 'Send a test message', description: 'FeedSignal posts a test card to the channel so you can confirm delivery before relying on it.' },
      { step: 5, title: 'Start receiving alerts', description: 'Alerts post to Teams as MessageCards — per alert type per user, toggleable from Settings → Notifications.' },
    ],
  },

  {
    slug: 'email',
    name: 'Email Forwarding',
    tagline: 'Forward customer emails and let AI extract the insights',
    description: 'Simply forward customer feedback emails to your FeedSignal inbox. Our AI strips headers, identifies the original sender, and analyzes the content — from any email client.',
    status: 'available',
    color: 'accent',
    gradient: 'from-accent to-chart-3',
    hoverShadow: 'hover:shadow-accent/10',
    hoverBorder: 'hover:border-accent/30',
    heroMessage: 'No API integration needed. Just forward any customer email to your FeedSignal inbox address and our AI does the rest — extracts the feedback, identifies the sender, detects sentiment, and categorizes it automatically.',
    howItWorks: [
      { step: '1', title: 'Get Your Inbox Address', description: 'Every FeedSignal workspace gets a unique email address for receiving forwarded feedback.' },
      { step: '2', title: 'Forward Customer Emails', description: 'Forward feedback emails from Gmail, Outlook, Apple Mail, or any client. We strip forwarding headers automatically.' },
      { step: '3', title: 'AI Analyzes Content', description: 'The original message is extracted, sender identified, and content analyzed for sentiment, pain points, and feature requests.' },
    ],
    features: [
      { title: 'Universal Compatibility', description: 'Works with Gmail, Outlook, Apple Mail, Thunderbird, and any email client. We parse forwarding headers from all major providers.', icon: 'Mail' },
      { title: 'Smart Header Parsing', description: 'Our parser strips "Begin forwarded message", "From:", "Date:", and other forwarding artifacts. Only the real content is analyzed.', icon: 'FileText' },
      { title: 'Sender Detection', description: 'Original sender email and name are automatically extracted from forwarding headers, so you know who the feedback is from.', icon: 'UserCheck' },
      { title: 'Keyword Matching', description: 'Set up keyword triggers to only capture emails containing specific terms — or monitor all forwarded emails.', icon: 'Search' },
      { title: 'No Setup Required', description: 'No API keys, no OAuth, no webhooks to configure. Just forward an email and it works instantly.', icon: 'Zap' },
      { title: 'Bulk Forwarding', description: 'Set up email rules in your client to auto-forward specific emails to FeedSignal. Hands-free feedback collection.', icon: 'Layers' },
    ],
    useCases: [
      { persona: 'Solo Founder', role: 'Bootstrapped SaaS', quote: 'I get customer emails all day. Now I just forward them to FeedSignal and check the dashboard once a week. It\'s like having a customer research team for free.', icon: 'Rocket' },
      { persona: 'Sales Team Lead', role: 'B2B startup, 20 reps', quote: 'I asked my sales team to forward any "lost deal" emails to FeedSignal. Within a month, we had a clear picture of why prospects were churning — pricing confusion was #1.', icon: 'Target' },
      { persona: 'Customer Support Lead', role: 'E-commerce, 500+ emails/day', quote: 'We set up an Outlook rule to auto-forward all complaint emails. FeedSignal\'s AI categorizes them way better than our manual tagging — and it catches things we missed.', icon: 'Headphones' },
    ],
    faqs: SHARED_FAQS,
    setupSteps: [
      { step: 1, title: 'Go to Settings → Integrations', description: 'Navigate to your FeedSignal dashboard and open the Integrations page.' },
      { step: 2, title: 'Find your unique inbox address', description: 'Your workspace has a dedicated email address for receiving forwarded feedback.' },
      { step: 3, title: 'Create an email feedback source', description: 'Set up a feedback source with email type and configure keyword triggers if needed.' },
      { step: 4, title: 'Forward your first email', description: 'Forward a customer email from any client. FeedSignal processes it within seconds.' },
      { step: 5, title: 'Optional: Set up auto-forwarding', description: 'Create email rules in Gmail/Outlook to automatically forward specific emails to FeedSignal.' },
    ],
  },
  {
    slug: 'linear',
    name: 'Linear',
    tagline: 'Turn issue tracker comments into actionable product feedback',
    description: 'Connect Linear and let FeedSignal analyze issue comments, bug reports, and feature requests — surfacing customer sentiment and product patterns your team would otherwise miss.',
    status: 'available',
    color: 'chart-5',
    gradient: 'from-[#5E6AD2] to-[#8B94E8]',
    hoverShadow: 'hover:shadow-[#5E6AD2]/10',
    hoverBorder: 'hover:border-[#5E6AD2]/30',
    heroMessage: 'Your Linear issues are full of customer feedback hiding in comments and descriptions. FeedSignal connects to Linear and automatically extracts sentiment, pain points, and feature requests — giving your product team a clear signal from the noise.',
    howItWorks: [
      { step: '1', title: 'Connect Linear', description: 'Authorize FeedSignal via OAuth in one click. We securely connect to your Linear workspace.' },
      { step: '2', title: 'Issues Flow In', description: 'New issue comments, status changes, and labels are sent to FeedSignal via webhooks in real-time.' },
      { step: '3', title: 'AI Finds Patterns', description: 'Our AI analyzes every comment for sentiment, categorizes feedback, and surfaces the most impactful product insights.' },
    ],
    features: [
      { title: 'Issue Comment Analysis', description: 'Every comment on Linear issues is analyzed for customer sentiment, pain points, and feature requests — automatically.', icon: 'MessageSquare' },
      { title: 'Label-Based Filtering', description: 'Choose which issues to monitor by label. Only capture feedback from customer-facing issues, bug reports, or specific projects.', icon: 'Tags' },
      { title: 'Team Mapping', description: 'Map Linear teams to FeedSignal categories. Route feedback from different teams to the right dashboard views.', icon: 'Users' },
      { title: 'Status Tracking', description: 'Track how feedback correlates with issue status. See which customer pain points are being addressed and which are stuck.', icon: 'TrendingUp' },
      { title: 'Issue Templates', description: 'Create issues back in Linear from FeedSignal with customizable templates — including sentiment data and customer context.', icon: 'FileText' },
      { title: 'Real-Time Webhooks', description: 'Instant data flow via Linear webhooks with signature verification. No polling, no delays — feedback appears in seconds.', icon: 'Zap' },
    ],
    useCases: [
      { persona: 'Product Manager', role: 'B2B SaaS, 200+ issues/week', quote: 'We had feature requests scattered across hundreds of Linear issues. FeedSignal now surfaces the top requests with sentiment context — we prioritize based on data, not gut feeling.', icon: 'Layers' },
      { persona: 'Engineering Lead', role: 'Developer tools startup', quote: 'Bug reports from customers often have valuable product feedback buried in the comments. FeedSignal catches patterns we never would have seen — like 3 different customers hitting the same workflow issue.', icon: 'Rocket' },
      { persona: 'Customer Success Manager', role: 'Enterprise SaaS', quote: 'I used to manually scan Linear for customer-reported issues. Now I check FeedSignal\'s dashboard and instantly see which accounts are frustrated and what they need fixed.', icon: 'Heart' },
    ],
    faqs: SHARED_FAQS,
    setupSteps: [
      { step: 1, title: 'Go to Settings → Integrations', description: 'Navigate to your FeedSignal dashboard and open the Integrations page.' },
      { step: 2, title: 'Click "Connect Linear"', description: 'You\'ll be redirected to Linear to authorize FeedSignal via OAuth. Approve the connection — credentials and webhook secrets are encrypted at rest.' },
      { step: 3, title: 'Configure team mappings', description: 'Map your Linear teams to FeedSignal categories so feedback is automatically organized.' },
      { step: 4, title: 'Set up a feedback source', description: 'Create a Linear feedback source and configure which labels or keywords to monitor.' },
      { step: 5, title: 'Start analyzing issues', description: 'Issue comments flow in automatically. View insights on your dashboard within minutes.' },
    ],
  },
  {
    slug: 'jira',
    name: 'Jira',
    tagline: 'Two-way sync with the Jira issues your team already tracks',
    description: 'Connect Jira Cloud and create issues directly from feedback items — with sentiment, customer context, and a link back to the original feedback. When your team moves an issue to In Progress or Done, FeedSignal syncs that status back onto the feedback automatically.',
    status: 'available',
    color: 'chart-2',
    gradient: 'from-[#0052CC] to-[#2684FF]',
    hoverShadow: 'hover:shadow-[#0052CC]/10',
    hoverBorder: 'hover:border-[#0052CC]/30',
    heroMessage: 'Stop copy-pasting customer feedback into Jira by hand. FeedSignal connects to Jira Cloud with a personal API token and lets you create fully-linked issues — with sentiment and customer context attached — straight from any feedback item.',
    howItWorks: [
      { step: '1', title: 'Connect Jira', description: 'Paste your Jira site URL, account email, and a personal API token to authorize FeedSignal — no OAuth redirect required.' },
      { step: '2', title: 'Create Issues from Feedback', description: 'Pick a project and issue type, then create a Jira issue directly from any feedback item — pre-filled with the feedback content and AI context.' },
      { step: '3', title: 'Track the Link & Sync Status Back', description: 'FeedSignal keeps a link between the feedback item and the Jira issue. Turn on status-sync and the feedback item follows the issue — moving to Resolved when the ticket is done, all on its own.' },
    ],
    features: [
      { title: 'Token-Based Connection', description: 'Connect with a personal Atlassian API token — no OAuth app to register, no admin approval workflow required.', icon: 'KeyRound' },
      { title: 'One-Click Issue Creation', description: 'Turn any feedback item into a Jira issue in a couple of clicks, pre-filled with title, description, and customer context.', icon: 'FileText' },
      { title: 'Project & Issue-Type Picker', description: 'Choose which Jira project and issue type (Bug, Task, Story) each issue is created in — no hardcoded defaults.', icon: 'Tags' },
      { title: 'Feedback-to-Issue Linking', description: 'Every created issue is linked back to the originating feedback item, so context is never lost.', icon: 'RefreshCw' },
      { title: 'Two-Way Status Sync', description: 'Opt in and FeedSignal keeps the feedback item in step with your linked Jira issues — a 15-minute poll works behind any firewall, and an optional real-time webhook applies the change the moment the issue moves, never overwriting a status you set by hand.', icon: 'RefreshCw' },
      { title: 'Cloud-Native', description: 'Built for Jira Cloud (*.atlassian.net) using the official REST API v3 with Basic auth.', icon: 'Zap' },
    ],
    useCases: [
      { persona: 'Product Manager', role: 'B2B SaaS, Jira-based roadmap', quote: 'We used to manually re-type customer complaints into Jira tickets. Now I create the issue right from the feedback card and the customer context comes with it.', icon: 'Layers' },
      { persona: 'Engineering Lead', role: 'Platform team', quote: 'Every bug report that turns into a Jira ticket keeps a link back to the original feedback, so nobody has to ask "wait, who reported this?"', icon: 'Rocket' },
    ],
    faqs: JIRA_FAQS,
    setupSteps: [
      { step: 1, title: 'Go to Settings → Integrations', description: 'Navigate to your FeedSignal dashboard and open the Integrations page.' },
      { step: 2, title: 'Mint an Atlassian API token', description: 'Go to id.atlassian.com → Security → API tokens, and create a new API token for your Atlassian account.' },
      { step: 3, title: 'Paste your credentials into FeedSignal', description: 'In FeedSignal, go to Settings → Integrations → Jira and paste your Jira site URL (e.g. your-company.atlassian.net), your Atlassian account email, and the API token you just created.' },
      { step: 4, title: 'FeedSignal validates the connection', description: 'FeedSignal verifies the token against your Jira site and encrypts it at rest. You\'ll see a connected status once it succeeds.' },
      { step: 5, title: 'Create your first issue', description: 'Open any feedback item, choose "Create Jira Issue," pick a project and issue type, and FeedSignal creates a linked Jira issue for you.' },
    ],
  },

  {
    slug: 'asana',
    name: 'Asana',
    tagline: 'Turn feedback into Asana tasks your team already works from',
    description: 'Connect Asana with a personal access token and create tasks directly from feedback items — with sentiment, customer context, and a link back to the original feedback included automatically.',
    status: 'available',
    color: 'chart-1',
    gradient: 'from-[#F06A6A] to-[#FF9C9C]',
    hoverShadow: 'hover:shadow-[#F06A6A]/10',
    hoverBorder: 'hover:border-[#F06A6A]/30',
    heroMessage: 'Stop copy-pasting customer feedback into Asana by hand. FeedSignal connects to Asana with a personal access token and lets you create tasks — with sentiment and customer context attached — straight from any feedback item.',
    howItWorks: [
      { step: '1', title: 'Connect Asana', description: 'Paste a personal access token to authorize FeedSignal — no OAuth redirect required.' },
      { step: '2', title: 'Create Tasks from Feedback', description: 'Pick a workspace and project, then create an Asana task directly from any feedback item — pre-filled with the feedback content and AI context.' },
      { step: '3', title: 'Track the Link & Sync Status Back', description: 'FeedSignal keeps a link between the feedback item and the Asana task — turn on status-sync and the feedback follows the task, moving to Resolved when it is completed (and back if it reopens).' },
    ],
    features: [
      { title: 'Token-Based Connection', description: 'Connect with a personal Asana access token — no OAuth app to register, no admin approval workflow required.', icon: 'KeyRound' },
      { title: 'One-Click Task Creation', description: 'Turn any feedback item into an Asana task in a couple of clicks, pre-filled with name, notes, and customer context.', icon: 'FileText' },
      { title: 'Workspace & Project Picker', description: 'Choose which Asana workspace and project each task is created in — no hardcoded defaults.', icon: 'Tags' },
      { title: 'Feedback-to-Task Linking', description: 'Every created task is linked back to the originating feedback item, so context is never lost.', icon: 'RefreshCw' },
      { title: 'Duplicate-Safe', description: 'Creating a task twice from the same feedback item surfaces the existing linked task instead of silently duplicating it.', icon: 'Shield' },
      { title: 'Status Sync (Poll + Real-Time)', description: 'Opt in and FeedSignal follows linked Asana tasks — the feedback item moves to Resolved when the task is completed, via a 15-minute poll plus an optional real-time webhook.', icon: 'RefreshCw' },
    ],
    useCases: [
      { persona: 'Product Manager', role: 'B2B SaaS, Asana-based roadmap', quote: 'We used to manually re-type customer complaints into Asana tasks. Now I create the task right from the feedback card and the customer context comes with it.', icon: 'Layers' },
      { persona: 'Customer Success Manager', role: 'Mid-market SaaS', quote: 'Every escalation that turns into an Asana task keeps a link back to the original feedback, so nobody has to ask "wait, who reported this?"', icon: 'Heart' },
    ],
    faqs: ASANA_FAQS,
    setupSteps: [
      { step: 1, title: 'Go to Settings → Integrations', description: 'Navigate to your FeedSignal dashboard and open the Integrations page.' },
      { step: 2, title: 'Mint an Asana Personal Access Token', description: 'In Asana, go to your profile settings → Apps → Manage Developer Apps → Create new token, and copy it.' },
      { step: 3, title: 'Paste your token into FeedSignal', description: 'In FeedSignal, go to Settings → Integrations → Asana and paste the personal access token you just created.' },
      { step: 4, title: 'FeedSignal validates the connection', description: 'FeedSignal verifies the token against your Asana account and encrypts it at rest. You\'ll see a connected status once it succeeds.' },
      { step: 5, title: 'Create your first task', description: 'Open any feedback item, choose "Create Asana Task," pick a workspace and project, and FeedSignal creates a linked Asana task for you.' },
    ],
  },
  {
    slug: 'hubspot',
    name: 'HubSpot',
    tagline: 'Sync CRM data with feedback — and push health scores back to HubSpot',
    description: 'Connect HubSpot to enrich your feedback data with CRM context — see which customers are giving feedback, their account value, and how sentiment correlates with revenue. Opt in to push each customer\'s health score back into HubSpot automatically.',
    status: 'available',
    color: 'destructive',
    gradient: 'from-[#FF7A59] to-[#FF957A]',
    hoverShadow: 'hover:shadow-[#FF7A59]/10',
    hoverBorder: 'hover:border-[#FF7A59]/30',
    heroMessage: 'Combine CRM intelligence with feedback analysis for a complete view of your customer relationships — and optionally push FeedSignal\'s health score straight back into a HubSpot contact property, so your CRM stays in sync automatically.',
    howItWorks: [
      { step: '1', title: 'Connect HubSpot', description: 'Paste a HubSpot private-app access token to authorize FeedSignal — no OAuth redirect required.' },
      { step: '2', title: 'Enrich Feedback Data', description: 'Customer feedback is automatically linked to HubSpot contacts and deals by email address.' },
      { step: '3', title: 'Push Health Scores Back (optional)', description: 'Opt in to writeback and FeedSignal pushes each customer\'s health score into a HubSpot contact property you choose.' },
    ],
    features: [
      { title: 'Contact Matching', description: 'Feedback is automatically matched to HubSpot contacts by email address.', icon: 'Users' },
      { title: 'Deal Context', description: 'See deal stage, value, and history alongside customer feedback.', icon: 'DollarSign' },
      { title: 'Revenue Impact', description: 'Prioritize feedback from high-value accounts. Know which pain points affect your biggest customers.', icon: 'TrendingUp' },
      { title: 'Lifecycle Tracking', description: 'Track how customer sentiment evolves across their lifecycle — from prospect to long-term customer.', icon: 'BarChart3' },
      { title: 'Health-Score Writeback', description: 'Opt-in bidirectional sync pushes FeedSignal\'s calculated health score back into a HubSpot contact property you choose — kept in sync automatically as scores change.', icon: 'RefreshCw' },
      { title: 'Churn Labels from Lost Renewals', description: 'Opt in and FeedSignal reads closed-lost deals from the renewal pipelines you name and proposes them as churn labels. They are suggestions, never labels: each one waits in a review queue for a human to confirm or reject, because a lost renewal is not always a churn. Off until you configure it — name no pipelines and nothing is suggested.', icon: 'ClipboardCheck' },
    ],
    useCases: [
      { persona: 'Customer Success Manager', role: 'B2B SaaS, HubSpot CRM', quote: 'Our reps live in HubSpot. Now the health score shows up right on the contact record, so nobody has to context-switch to FeedSignal to know an account is at risk.', icon: 'Heart' },
      { persona: 'RevOps Lead', role: 'Series A SaaS', quote: 'Deal value and feedback sentiment used to live in two different tools. FeedSignal ties them together in HubSpot, so we prioritize fixes by revenue impact, not gut feel.', icon: 'TrendingUp' },
    ],
    faqs: SHARED_FAQS,
    setupSteps: [
      { step: 1, title: 'Go to Settings → Integrations', description: 'Navigate to your FeedSignal dashboard and open the Integrations page.' },
      { step: 2, title: 'Create a HubSpot private app', description: 'In HubSpot, create a private app and copy its access token. Grant crm.objects.contacts.read (and crm.objects.deals.read) scopes.' },
      { step: 3, title: 'Paste the token into FeedSignal', description: 'Connect HubSpot from Settings → Integrations by pasting the private-app token. FeedSignal validates and encrypts it immediately.' },
      { step: 4, title: 'Optional: enable health-score writeback', description: 'Create a number-type custom contact property in HubSpot, grant crm.objects.contacts.write on your private-app token, then enter the property name in FeedSignal to turn on writeback.' },
      { step: 5, title: 'Start syncing', description: 'Feedback is enriched with CRM context automatically. If writeback is enabled, each customer\'s health score pushes to HubSpot as it updates.' },
    ],
  },

];

export function getIntegration(slug: string): Integration | undefined {
  return integrations.find((i) => i.slug === slug);
}

export function getAvailableIntegrations(): Integration[] {
  return integrations.filter((i) => i.status === 'available');
}

export function getComingSoonIntegrations(): Integration[] {
  return integrations.filter((i) => i.status === 'coming_soon');
}
