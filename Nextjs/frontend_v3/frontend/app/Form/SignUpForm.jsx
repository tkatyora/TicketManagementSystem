'use client'
import { useState } from 'react';
import { useRouter } from 'next/navigation';
import axiosInstance from '@/app/ApiServices/axiosConfig';
import { Toaster, toast } from 'react-hot-toast';

const SignUp = () => {
  const [fullName, setFullName] = useState('');
  const [email, setEmail] = useState('');
  const [phoneNumber, setPhoneNumber] = useState('');
  const [password, setPassword] = useState('');
  const [confirmPassword, setConfirmPassword] = useState('');
  const [accountType, setAccountType] = useState('personal');
  const [nationalId, setNationalId] = useState('');
  const [errors, setErrors] = useState({});
  const router = useRouter();

  const handleSignUp = async (e) => {
    e.preventDefault();
    try {
    
  
  
      const response = await axiosInstance.post('/auth_api/stsusers/', {
        full_name: fullName,
        email,
        phone_number: phoneNumber,
        password,
        password2: confirmPassword,
        account_type: accountType === 'bussiness' ? 'bussiness' : 'personal', 
        national_id: accountType === 'bussiness' ? nationalId : undefined
      });
      const data = response.data;
      console.log('Customer registered successfully:');
      // console.log(data)
      router.push('activate');
    } catch (error) {
      if (error.response && error.response.data) {
        setErrors(error.response.data);
        const errors = error.response.data;
        for (const key in errors) {
          if (errors.hasOwnProperty(key)) {
            if (Array.isArray(errors[key])) {
              toast.error(`${key}: ${errors[key].join(', ')}`);
            } else {
              toast.error(`${key}: ${errors[key]}`);
            }
          }
        }
      } else {
        console.error('Errors:', error);
        toast.error('Network Issues Please. Try Again Later.');
      }
    }
  };

  return (
    <>
      <Toaster />
      <div className="bg-white p-8 mt-7 mb-7 rounded-lg shadow-lg max-w-md w-full">
        <h1 className="text-2xl font-bold mb-1">Effective Way to Handle  Shows</h1>
        <h3 className=" text-center font-bold mb-4">Create Account</h3>
        <form onSubmit={handleSignUp} className="flex flex-col mb-5">
        <div className="mb-4">
            <label htmlFor="accountType" className="block text-sm font-semibold mb-1">
              Account Type <span className="text-red-500">*</span>
            </label>
            <select
              id="accountType"
              value={accountType}
              onChange={(e) => setAccountType(e.target.value)}
              required
              className="form-select w-full p-2 pr-7 border rounded-lg focus:outline-none focus:ring focus:ring-blue-500"
            >
              <option value="personal">Personal Account</option>
              <option value="bussiness">Business Account</option>
            </select>
          </div>
          <div className="mb-2">
            <label htmlFor="fullName" className="block text-sm font-semibold mb-2">
            Full Name  <span className="text-red-500">*</span>
            </label>
            <input
              type="text"
              id="fullName"
              value={fullName}
              onChange={(e) => setFullName(e.target.value)}
              placeholder="Enter Full Name"
              required
              className="form-input w-full p-2 pr-4 border rounded-lg focus:outline-none focus:ring focus:ring-blue-500"
            />
          </div>

          <div className="mb-6">
            <label htmlFor="email" className="block text-sm font-semibold mb-2">
              Email <span className="text-red-500">*</span>
            </label>
            <input
              type="email"
              id="email"
              required
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              placeholder="Enter Email"
              className={`form-input w-full p-2 pr-4 border rounded-lg focus:outline-none focus:ring focus:ring-blue-500 ${errors.email ? 'border-red-500' : ''}`}
            />
             {errors.email && <p className="text-red-500 text-sm">{errors.email.join(', ')}</p>}
          </div>
          <div className="mb-6">
            <label htmlFor="phoneNumber" className="block text-sm font-semibold mb-2">
              Phone Number  <span className="text-red-500">*</span>
            </label>
            <input
              type="text"
              id="phoneNumber"
              value={phoneNumber}
              onChange={(e) => setPhoneNumber(e.target.value)}
              placeholder="Enter Phone Number"
              required
              className={`form-input w-full p-2 pr-4 border rounded-lg focus:outline-none focus:ring focus:ring-blue-500 ${errors.phone_number ? 'border-red-500' : ''}`}
            />
            {errors.phone_number && <p className="text-red-500 text-sm">{errors.phone_number.join(', ')}</p>}
          </div>
          {accountType === 'bussiness' && (
            <div className="mb-2">
              <label htmlFor="nationalId" className="block text-sm font-semibold mb-1">
                National ID <span className="text-red-500">*</span>
              </label>
              <input
                type="text"
                id="nationalId"
                value={nationalId}
                onChange={(e) => setNationalId(e.target.value)}
                placeholder="Enter National ID"
                required
                className={`form-input w-full p-2 pr-4 border rounded-lg focus:outline-none focus:ring focus:ring-blue-500 ${errors.national_id ? 'border-red-500' : ''}`}
                />
                {errors.national_id && <p className="text-red-500 text-sm">{errors.national_id.join(', ')}</p>}
            </div>
          )}
          <div className="mb-6">
            <label htmlFor="password" className="block text-sm font-semibold mb-2">
              Password  <span className="text-red-500">*</span>
            </label>
            <input
              type="password"
              id="password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              placeholder="Create Password"
              required
              className={`form-input w-full p-2 pr-4 border rounded-lg focus:outline-none focus:ring focus:ring-blue-500 ${errors.password ? 'border-red-500' : ''}`}
              />
              {errors.password && <p className="text-red-500 text-sm">{errors.password.join(', ')}</p>}
          </div>
          <div className="mb-6">
            <label htmlFor="confirmPassword" className="block text-sm font-semibold mb-2">
              Confirm Password  <span className="text-red-500">*</span>
            </label>
            <input
              type="password"
              id="confirmPassword"
              value={confirmPassword}
              onChange={(e) => setConfirmPassword(e.target.value)}
              placeholder="Confirm Password"
              required
              className={`form-input w-full p-2 pr-4 border rounded-lg focus:outline-none focus:ring focus:ring-blue-500 ${errors.password2 ? 'border-red-500' : ''}`}
            />
            {errors.password2 && <p className="text-red-500 text-sm">{errors.password2.join(', ')}</p>}
          </div>
          <button type="submit" className="py-2 px-4 bg-blue-600 text-white rounded-lg">
            Create Account
          </button>
        </form>
      </div>
    </>
  );
};

export default SignUp;
