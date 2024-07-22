"use client"; 
import React, { useState } from 'react';
import { HomeIcon, ChartBarIcon, ShoppingCartIcon, InboxInIcon, LogoutIcon, UserCircleIcon } from '@heroicons/react/outline';
import Image from 'next/image';
import TopNavbar from "@/app/componets/TopNavbar"
import LogoutButton from "@/app/componets/logout"

const PersonalDashboard = () => {
  const [open, setOpen] = useState(false);

  const user = {
    name: '',
    email: '',
  };

  const shows = [
    { id: 1, title: 'Show A' },
    { id: 2, title: 'Show B' },
    { id: 1, title: 'Show A' },
    { id: 2, title: 'Show B' },
    { id: 1, title: 'Show A' },
    { id: 2, title: 'Show B' },
   
  ];

  const handleAddToCart = (id) => {
    
    console.log(`Added show ${id} to cart`);
  };

  const handleViewDetails = (id) => {
    
    console.log(`Viewing details for show ${id}`);
  };

  return (
    <div className="flex flex-col h-screen bg-gray-100">
      <TopNavbar user={user} />

      <div className="flex flex-1">
        
        <aside className={`w-64  bg-white shadow-md ${open ? 'block' : 'hidden'} sm:block`}>
          <div className="p-6">
            <h1 className="text-2xl font-semibold text-gray-800">Dashboard</h1>
            <nav className="mt-6">
              <div className="flex items-center px-4 py-2 mt-5 text-gray-600 transition-colors duration-300 transform rounded-lg hover:bg-gray-200 hover:text-gray-700">
                <HomeIcon className="w-6 h-6" />
                <span className="mx-4">Home</span>
              </div>
              <div className="flex items-center px-4 py-2 mt-5 text-gray-600 transition-colors duration-300 transform rounded-lg hover:bg-gray-200 hover:text-gray-700">
                <ShoppingCartIcon className="w-6 h-6" />
                <span className="mx-4">My Cart</span>
              </div>
              <div className="flex items-center px-4 py-2 mt-5 text-gray-600 transition-colors duration-300 transform rounded-lg hover:bg-gray-200 hover:text-gray-700">
                <ChartBarIcon className="w-6 h-6" />
                <span className="mx-4">Trending Shows</span>
              </div>
              <div className="flex items-center px-4 py-2 mt-5 text-gray-600 transition-colors duration-300 transform rounded-lg hover:bg-gray-200 hover:text-gray-700">
                <InboxInIcon className="w-6 h-6" />
                <span className="mx-4">Messages</span>
              </div>
              <div className="flex items-center px-4 py-2 mt-5 text-gray-600 transition-colors duration-300 transform rounded-lg hover:bg-gray-200 hover:text-gray-700">
                <UserCircleIcon className="w-6 h-6" />
                <span className="mx-4">User Profile</span>
              </div>
              <LogoutButton />
            </nav>
          </div>
        </aside>

        {/* Main Content */}
        <div className="flex-1 p-6 overflow-y-auto">
          {/* Show List */}
          <div className="space-y-4">
            {shows.map((show) => (
              <div key={show.id} className="bg-white p-6 rounded-lg shadow-lg flex flex-col items-center space-y-4">
                <Image
                  src="/Images/code.jpg"
                  alt={show.title}
                  width={150}
                  height={150}
                  className="object-cover rounded-full border-2 border-gray-200 shadow-md"
                />
                <h2 className="text-xl font-bold text-gray-800">{show.title}</h2>
                <div className="flex space-x-4">
                  <button
                    onClick={() => handleAddToCart(show.id)}
                    className="bg-blue-500 text-white px-4 py-2 rounded-lg hover:bg-blue-600 transition duration-300"
                  >
                    Add to Cart
                  </button>
                  <button
                    onClick={() => handleViewDetails(show.id)}
                    className="bg-gray-200 text-gray-800 px-4 py-2 rounded-lg hover:bg-gray-300 transition duration-300"
                  >
                    View Details
                  </button>
                </div>
              </div>
            ))}
          </div>
        </div>
      </div>
    </div>
  );
};

export default PersonalDashboard;
