"use client"
import { useState } from 'react';
import { useRouter } from 'next/navigation';
import axiosInstance from '@/app/ApiServices/axiosConfig'
import toast from 'react-hot-toast';
import { Toaster } from 'react-hot-toast';
import Loader from 'react-loader-spinner';


const ActivateAccount = () => {
  const [activationCode, setActivationCode] = useState('');
  const [error, setError] = useState('');
  const [successMessage, setSuccessMessage] = useState('');
  const router = useRouter();

  const handleActivateAccount = async (e) => {
    e.preventDefault();
    try {
      const response = await axiosInstance.post('/auth_api/activate/', {
         code: activationCode 
        });
        console.log(response.data)
        if (response.data.message === 'activated.') {
          setSuccessMessage('User already activated.');
          toast.success("User Already Activated")
          toast.loading("Redirecting To Sign In Page in 3 seconds")
          setTimeout(() => {
            router.push('/app');
          }, 3000);
        } else {
          setSuccessMessage(response.data.message);
          toast.success(response.data.message)
          toast.loading('Redirecting to Sign In Page in 3 seconds', {
            duration: 3000,
          });
          setTimeout(() => {
            router.push('/app');
          }, 3000);
        }
    } catch (error) {
      if (error.response && error.response.data) {
         setError(error.response.data.error);
         toast.error(error.response.data.error)
      } else {
        console.error('Errors:', error);
      }
      
    }
  };

  return (
    <>
         <Toaster />
      <main className="relative h-screen flex flex-col items-center justify-center bg-gradient-to-r from-blue-400 via-purple-500 to-pink-500">
      <div className="bg-white p-8 mt-7 mb-7 content-center rounded-lg shadow-lg max-w-md w-full">
      <h1 className="text-2xl font-bold mb-1">Activate Your Account</h1>
      <form onSubmit={handleActivateAccount} className="flex flex-col mb-5">
        <div className="mb-6">
          <p className='font-semibold mb-4 text-blue-700'>Activation code Send to your Email</p>
          <label htmlFor="activationCode" className="block text-sm font-semibold mb-2">
            Activation Code
          </label>
          <input
            type="text"
            name='code'
            id="activationCode"
            value={activationCode}
            onChange={(e) => setActivationCode(e.target.value)}
            placeholder="Enter Activation Code"
            required
                className={`form-input w-full p-2 pr-4 border rounded-lg focus:outline-none focus:ring focus:ring-blue-500 ${error ? 'border-red-500' : ''}`}
          />
        </div>
        {error && <p className="text-red-500 mb-4">{error}</p>}
        {successMessage && <p className="text-green-500 mb-4">{successMessage}</p>}
        <button type="submit" className="py-2 px-4 bg-blue-600 text-white rounded-lg">
          Activate Account
        </button>
      </form>
    </div>
      </main>
    
    </>
   
  );
};

export default ActivateAccount;
