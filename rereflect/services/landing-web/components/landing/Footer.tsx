import Link from 'next/link';
import { Logo } from '@rereflect/ui';

const GITHUB_URL = 'https://github.com/Akgithub2028/FeedSignal';

export default function Footer() {
  return (
    <footer className="lp-footer">
      <div className="lp-footer-grid">
        <div>
          <Link href="/" className="lp-logo">
            <Logo size="md" />
            <span>
              <span className="text-accent">Feed</span>Signal
            </span>
          </Link>
          <p className="lp-footer-tag">
            Customer feedback, analyzed. Open source, self-hosted, and yours.
          </p>
          <a className="mt-6 inline-block" href="mailto:aayaannkausar@gmail.com">Contact support</a>
        </div>

        <div className="lp-footer-col">
          <h4>Product</h4>
          <Link href="/#features">Features</Link>
          <Link href="/integrations">Integrations</Link>
          <Link href="/blog">Blog</Link>
        </div>

        <div className="lp-footer-col">
          <h4>Open source</h4>
          <a href={GITHUB_URL} target="_blank" rel="noopener noreferrer">
            GitHub
          </a>
          <a href={`${GITHUB_URL}/blob/main/rereflect/docs/SELF_HOSTING.md`} target="_blank" rel="noopener noreferrer">
            Self-host guide
          </a>
          <Link href="/privacy">Privacy</Link>
          <Link href="/terms">Terms</Link>
        </div>

        <div className="lp-footer-col">
          <h4>Stack</h4>
          <span className="text-[0.8125rem] text-[var(--content-tertiary)]">FastAPI · Celery</span>
          <span className="text-[0.8125rem] text-[var(--content-tertiary)]">PostgreSQL · Redis</span>
          <span className="text-[0.8125rem] text-[var(--content-tertiary)]">Next.js · Tailwind</span>
        </div>
      </div>

      <div className="lp-footer-bottom">
        <span>© {new Date().getFullYear()} FeedSignal · Maintained by <a href="https://github.com/Akgithub2028" target="_blank" rel="noopener noreferrer">Akgithub2028</a></span>
        <span>MIT licensed · self-hosted</span>
      </div>
    </footer>
  );
}
