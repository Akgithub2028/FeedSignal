import type { Metadata } from "next";
import { Geist, Geist_Mono } from "next/font/google";
import "./globals.css";
import "./landing.css";

// Geist / Geist Mono are the closest freely-licensed analogues to the
// neo-grotesque + technical-mono pairing the schematic layout is built on.
const geist = Geist({
  subsets: ["latin"],
  weight: ["300", "400", "500", "600"],
  variable: "--font-sans",
  display: "swap",
});

const geistMono = Geist_Mono({
  subsets: ["latin"],
  weight: ["400", "500"],
  variable: "--font-mono",
  display: "swap",
});

export const metadata: Metadata = {
  applicationName: "FeedSignal",
  verification: { google: "G8VZIRu29qZMEn4SmQ7e9C6bQgRMIpA-cY3dJJM_xPw" },
  creator: "Akgithub2028",
  authors: [{ name: "Akgithub2028", url: "https://github.com/Akgithub2028" }],
  metadataBase: new URL("https://feed-signal-ochre.vercel.app"),
  title: "FeedSignal - Open-Source Customer Feedback Analysis",
  description: "Self-hosted, MIT-licensed AI feedback analysis. Sentiment, pain points, feature requests, churn prediction, and 6+ integrations — fully unlocked, no vendor lock-in. Bring your own LLM key or run free on VADER.",
  keywords: ["open source", "self-hosted", "customer feedback", "sentiment analysis", "AI analysis", "feedback management", "customer insights", "BYOK", "MIT license"],
  openGraph: {
    title: "FeedSignal - Open-Source Customer Feedback Analysis",
    description: "Self-host FeedSignal on your own infrastructure. Every feature unlocked, MIT licensed, no tiers, no seats, no vendor lock-in.",
    url: "https://feed-signal-ochre.vercel.app",
    siteName: "FeedSignal",
    type: "website",
    images: [
      {
        url: "/images/logo.png",
        width: 1200,
        height: 630,
        alt: "FeedSignal - Open-Source Customer Feedback Analysis",
      },
    ],
  },
  twitter: {
    card: "summary_large_image",
    title: "FeedSignal - Open-Source Customer Feedback Analysis",
    description: "Self-host FeedSignal on your own infrastructure. Every feature unlocked, MIT licensed, no tiers, no seats, no vendor lock-in.",
    images: ["/images/logo.png"],

  },
};

// Inline script to prevent flash of unstyled content (FOUC)
// This runs synchronously before any CSS is applied
const themeInitScript = `
(function() {
  try {
    var theme = localStorage.getItem('theme') || 'system';
    var resolved = theme;
    if (theme === 'system') {
      resolved = window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light';
    }
    document.documentElement.setAttribute('data-theme', resolved);
    if (resolved === 'dark') {
      document.documentElement.classList.add('dark');
    } else {
      document.documentElement.classList.remove('dark');
    }
  } catch (e) {}
})();
`;

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en" suppressHydrationWarning>
      <head>
        {/* Preconnect to font providers for faster loading */}
        <link rel="preconnect" href="https://fonts.googleapis.com" />
        <link rel="preconnect" href="https://fonts.gstatic.com" crossOrigin="anonymous" />
        <script dangerouslySetInnerHTML={{ __html: themeInitScript }} />
      </head>
      <body className={`${geist.variable} ${geistMono.variable} antialiased font-sans`}>
        <div className="landing-dark min-h-screen">{children}</div>
      </body>
    </html>
  );
}