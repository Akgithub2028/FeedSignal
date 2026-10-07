import { NextResponse } from 'next/server';
import type { NextRequest } from 'next/server';

const MARKETING_DOMAIN = process.env.MARKETING_URL || process.env.NEXT_PUBLIC_MARKETING_URL || 'https://feed-signal-ochre.vercel.app';
const landingRoutes = ['/privacy', '/terms', '/changelog'];

export function middleware(request: NextRequest) {
  const pathname = request.nextUrl.pathname;

  // Skip middleware for static files and API routes
  if (
    pathname.startsWith('/_next') ||
    pathname.startsWith('/api') ||
    pathname.includes('.')
  ) {
    return NextResponse.next();
  }

  // Redirect landing routes to marketing domain
  if (landingRoutes.some(route => pathname === route || pathname.startsWith(`${route}/`))) {
    return NextResponse.redirect(new URL(`${pathname}${request.nextUrl.search}`, MARKETING_DOMAIN));
  }

  // Redirect root to dashboard
  if (pathname === '/') {
    return NextResponse.redirect(new URL('/dashboard', request.url));
  }

  return NextResponse.next();
}

export const config = {
  matcher: ['/((?!_next/static|_next/image|favicon.ico).*)'],
};
