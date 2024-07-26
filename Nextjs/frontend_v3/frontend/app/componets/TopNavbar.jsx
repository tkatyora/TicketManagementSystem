import Image from 'next/image';
import { Menu } from '@headlessui/react';
import { ChevronDownIcon } from '@heroicons/react/outline';
import Link from 'next/link';

const TopNavbar = ({  }) => {
    const  user = {
        'name':'Takudzwa',
        'email':"tkatyora7@gmail.com"
      }
    return (
        <div className="bg-gradient-to-r from-green-400 to-blue-500 shadow-md p-4 flex justify-between items-center">
            <h2 className="text-white text-xl font-bold">
                <Link href= '/dashboard/bussiness'>
                
                SecureTicketingSolution(sTs)
                </Link>
                </h2>

            <div className="flex items-center">
                <div className="ml-4">
                    <p className="font-semibold text-gray-100">Welcome {user.name}</p>
                </div>
            </div>
            
            <Menu as="div" className="relative">
                <Menu.Button className="flex items-center text-gray-100 hover:text-gray-200">
                    <Image
                        src="/Images/code.jpg"
                        alt="Profile Picture"
                        width={40}
                        height={40}
                        className="w-10 h-10 rounded-full mr-2"
                    />
                    <p className="font-semibold">{user.email}</p>
                    <ChevronDownIcon className="w-5 h-5 ml-1" />
                </Menu.Button>
                <Menu.Items className="absolute right-0 mt-2 bg-white border border-gray-200 rounded-lg shadow-lg w-48">
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
