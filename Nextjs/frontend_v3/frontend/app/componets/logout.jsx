import React, { useEffect, useState } from 'react';
import cookie from 'js-cookie';
import { useRouter } from 'next/navigation';
import {  LogoutIcon  } from '@heroicons/react/outline';
import axiosInstance from '../ApiServices/axiosConfig';

const LogoutButton = () => {
    const router = useRouter();
    const [error, setError] = useState('');

    const handleLogout = async () => {
        console.log('in log out')
        try {
            const token = cookie.get('auth_token');
            if (token) {
                await axiosInstance.post('/auth_api/logout/', {}, {
                    headers: {
                        Authorization: `Token ${token}`
                    }
                });
                cookie.remove('auth_token');
                router.push('/app');
            }
        } catch (error) {
        if (error.response && error.response.data && error.response.data.error) {
            setError(error.response.data.error);
            console.log(error.response.data.error,'error')
        } else {
            setError('Network Issues.Please Try again later');
            console.error('Error logging in:', error);
        }
    }
    };

    return (
        <div className="flex items-center px-4 py-2 mt-5 text-gray-600 transition-colors duration-300 transform rounded-lg hover:bg-gray-200 hover:text-gray-700">
                <LogoutIcon className="w-6 h-6" />
                <span className="mx-4">
                 <button onClick={handleLogout}>
                    Logout</button>
                </span>
     </div>
    );
};

export default LogoutButton;
