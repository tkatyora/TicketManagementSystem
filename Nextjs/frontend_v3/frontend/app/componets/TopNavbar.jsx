"use client"
import { useState } from 'react';
import Image from 'next/image';
import { Menu } from '@headlessui/react';
import { ChevronDownIcon } from '@heroicons/react/outline';
import Link from 'next/link';

const TopNavbar = ({ user }) => {
    return (
        <div className="bg-gray-900 shadow-md p-4 flex justify-between items-center ">
            <h2 className='text-white'>SecureTicketingSolution(sTs)</h2>
            
            <div className="flex items-center">
                
                <div className="ml-4">
                    <p className="font-semibold text-gray-800">{user.name}</p>
                    <p className="text-gray-600">{user.email}</p>
                </div>
            </div>
            <Menu as="div" className="relative">
                <Menu.Button className="flex items-center text-gray-600 hover:text-gray-800">
                <Image
                   src="/Images/code.jpg"
                    alt="Profile Picture"
                    width={40}
                    height={40}
                    className="w-10 h-10 rounded-full"
                />
                    <p className="font-semibold text-white">tkatyora</p>
                    <ChevronDownIcon className="w-5 h-5 text-white" />
                </Menu.Button>
                <Menu.Items className="absolute right-0 mt-2 bg-white border border-gray-200 rounded-lg shadow-lg">
                    <Menu.Item>
                        {({ active }) => (
                            <Link href="/profile" className={`block px-4 py-2 ${active ? 'bg-gray-100' : ''}`}>
                                Profile
                            </Link>
                      
                        )}
                    </Menu.Item>
                    <Menu.Item>
                        {({ active }) => (
                            <Link href="/settings" className={`block px-4 py-2 ${active ? 'bg-gray-100' : ''}`}>
                                Settings
                            </Link>
                        )}
                    </Menu.Item>
                    <Menu.Item>
                        {({ active }) => (
                            <Link href="/logout" className={`block px-4 py-2 ${active ? 'bg-gray-100' : ''}`}>
                                Logout
                            </Link>
                        )}
                    </Menu.Item>
                </Menu.Items>
            </Menu>
        </div>
    );
};

export default TopNavbar;
