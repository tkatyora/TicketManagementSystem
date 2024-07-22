"use client"
import Link from 'next/link'
import Image from 'next/image'
import { useState,React } from 'react'
import LogInForm from "@/app/Form/LogInForm"

const LogInPage = () => {
  const [messages, setMessages] = useState([
    { id: 1, text: 'Login successful!', type: 'success' },
    { id: 2, text: 'Invalid credentials.', type: 'warning' },
  ]);

  return (
    <div>
       <main className="relative h-screen flex flex-col items-center justify-center bg-gray-800">
      <Image
        src="/Images/code.jpg"
        alt="For Projects Guides"
        layout="fill"
        objectFit="cover"
        className="z-0 opacity-50"
      />
      <div className="relative z-10 w-full max-w-md p-8 bg-black bg-opacity-75 shadow-lg rounded-lg">
        <h5 className="text-white tex-lg font-semibold text-center">Welcome To</h5>
        <h4 className="text-center text-2xl font-semibold text-white">
          <Link href="/" className="text-decoration-none text-white">
              Secure<span className="text-blue-500">Ticketing</span>Solution
          </Link>
        </h4>
        {/* {messages.map((message) => (
          <div key={message.id} className="mt-4">
            <p className={`text-center ${message.type === 'warning' ? 'text-red-500' : 'text-green-500'}`}>
              {message.text}
            </p>
          </div>
        ))} */}
        <LogInForm/>
      </div>
    </main>
    </div>
  )
}

export default LogInPage