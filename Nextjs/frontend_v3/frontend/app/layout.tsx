import type { Metadata } from "next";
import { Inter } from "next/font/google";
import "./styles/globals.css";
import { Toaster } from 'react-hot-toast';


const inter = Inter({ subsets: ["latin"] });

export const metadata: Metadata = {
  title: "Secure Ticketing Solution",
  description: "App for secure ticcketing",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <head>
      <link href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css" rel="stylesheet" />

      </head>
    
      <body className={inter.className}>
      <Toaster />
        {children}</body>
    </html>
  );
}
