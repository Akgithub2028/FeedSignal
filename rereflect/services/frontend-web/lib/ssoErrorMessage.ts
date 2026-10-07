import { getSsoErrorMessage } from './oidcErrors';
import { getSamlErrorMessage, SAML_ERROR_CODES } from './samlErrors';

/**
 * Resolve a `?sso_error=<code>` query param to a friendly message, without a
 * protocol tag on the code itself. Deterministic, code-set based (no
 * magic-string compare against either map's generic-fallback text):
 *
 *   1. If `code` is one `getSamlErrorMessage` actually maps (SAML_ERROR_CODES
 *      — this covers both the SAML-only codes like `signature`/`assertion`
 *      and the codes SAML shares with OIDC but words differently, like
 *      `unverified`/`token`/`state`/`domain`/`config`/`disabled`), use the
 *      SAML wording.
 *   2. Otherwise fall back to the OIDC map (`getSsoErrorMessage`), which
 *      covers OIDC-only codes (e.g. `exchange`) and itself degrades to the
 *      generic "could not be completed" message for anything unknown.
 *
 * Exported for direct unit testing (see __tests__/page.test.tsx) independent
 * of rendering the whole page.
 */
export function resolveSsoErrorMessage(code: string): string {
  if (SAML_ERROR_CODES.has(code)) {
    return getSamlErrorMessage(code);
  }
  return getSsoErrorMessage(code);
}
