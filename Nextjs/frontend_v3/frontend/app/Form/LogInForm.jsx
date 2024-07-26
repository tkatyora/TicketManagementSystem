"use client"
import React from 'react'
import { useState ,useEffect } from 'react';
import { useRouter } from 'next/navigation';
import LogIn from "@/app/ApiServices/LogInApi"
import { Toaster, toast } from 'react-hot-toast';
import {UserCircleIcon  ,LockClosedIcon ,LockOpenIcon } from '@heroicons/react/outline';
import cookie from 'js-cookie';


const LogInForm = () => {
    const [usernameOrEmail, setUsernameOrEmail] = useState('');
    const [password, setPassword] = useState('');
    const [error, setError] = useState('');
    const router = useRouter();
  
    const handleSubmit = async (e) => {
      e.preventDefault();
      try {
        const data = await LogIn(usernameOrEmail, password);
        console.log(data.account_type)
        if (data.token) {
          toast.success("User Logged In Successfully."
          )
         
          cookie.set('auth_token', data.token, { expires: 1 });
          if (data.account_type === 'bussiness') {
            setTimeout(() => {
              router.push('/dashboard/bussiness');
            }, 10);
             
          } else {
            setTimeout(() => {
              router.push('/dashboard/personal');
            }, 10);

             
          }
      } else {
          setError('Invalid credentials');
      }
  } catch (error) {
      if (error.response && error.response.data && error.response.data.error) {
          setError(error.response.data.error);
      } else {
          setError('Network Issues.Please Try again later');
          console.error('Error logging in:', error);
      }
  }
    };
  
  
    return (
      <>
       <Toaster/>
         <form id="form-id" method="POST" className="mt-6 space-y-6" onSubmit={handleSubmit}>
        <div className="mb-2">
        {error && <p className="text-red-600 text-center mb-3">{error}</p>}
          <label htmlFor="username" className="block text-white text-sm font-semibold mb-2">Enter Username or Email</label>
          <div className="relative">
            <span className="absolute inset-y-0 left-0 flex items-center pl-3">
              <UserCircleIcon className="w-6 h-6 text-gray-400"/>
            </span>

            <input
              type="text"
              name="username_or_email"
              id="username_or_email"
              value={usernameOrEmail}
              onChange={(e) => setUsernameOrEmail(e.target.value)}
              required
              className="form-input w-full py-2 pl-12 pr-4 rounded-lg bg-gray-800 text-white placeholder-gray-400 focus:outline-none focus:ring focus:ring-blue-500"
              placeholder="Enter  username or email"
              autoFocus
            />
          </div>
        </div>
        <div className="mb-6">
          <label htmlFor="password" className="block text-white text-sm font-semibold mb-2">Password</label>
          <div className="relative">
            <span className="absolute inset-y-0 left-0 flex items-center pl-3">
              <LockClosedIcon className="w-6 h-6 text-gray-400"/>
              <LockOpenIcon className="w-6 h-6 text-gray-400 hidden"/>
            </span>
            <input
              type="password"
              name="password"
              id="password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              required
              className="form-input w-full py-2 pl-12 pr-4 rounded-lg bg-gray-800 text-white placeholder-gray-400 focus:outline-none focus:ring focus:ring-blue-500"
              placeholder="Enter your password"
            
            />
          </div>
        </div>



       
        <div className="text-center">
          <a href="/portal/sign_up" className="text-blue-500 hover:underline">
            Create a New Account
          </a>
        </div>
        <div className="text-center">
          <button type="submit" className="w-full py-2 px-4 bg-blue-500 hover:bg-blue-600 text-white rounded-md">
            Log In
          </button>
        </div>
      </form>
      </>
   
    )
}

export default LogInForm