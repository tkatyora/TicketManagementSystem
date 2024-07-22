import { NextResponse } from 'next/server';

export function middleware(request) {
  const token = request.cookies.get('auth_token');

  if (!token) {
    return NextResponse.redirect(new URL('/app', request.url));
  }

  return NextResponse.next();
}

export const config = {
  matcher: ['/dashboard/:path*','/portal/:path*'],  
};