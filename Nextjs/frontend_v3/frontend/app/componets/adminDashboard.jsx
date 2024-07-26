"use client"
import { useState } from 'react';
import { Doughnut, Line } from 'react-chartjs-2';
import { HomeIcon, UserCircleIcon, ChartBarIcon, ShoppingCartIcon, CameraIcon, InboxInIcon } from '@heroicons/react/outline';
import Link from 'next/link';
import { Chart as ChartJS, Title, Tooltip, Legend, ArcElement } from 'chart.js';
import TopNavbar from "@/app/componets/TopNavbar"
import LogoutButton from "@/app/componets/logout"

ChartJS.register(ArcElement, Title, Tooltip, Legend);
import { CategoryScale, LinearScale, PointElement, LineElement } from 'chart.js';
ChartJS.register(CategoryScale, LinearScale, PointElement, LineElement, Title, Tooltip, Legend);

const AdminDashboard = ({ user }) => {
    const [open, setOpen] = useState(false);
    

    const doughnutData = {
        labels: ['Red', 'Blue', 'Yellow'],
        datasets: [
            {
                label: '# of Votes',
                data: [12, 19, 3],
                backgroundColor: ['rgba(255, 99, 132, 0.2)', 'rgba(54, 162, 235, 0.2)', 'rgba(255, 206, 86, 0.2)'],
                borderColor: ['rgba(255, 99, 132, 1)', 'rgba(54, 162, 235, 1)', 'rgba(255, 206, 86, 1)'],
                borderWidth: 1,
            },
        ],
    };

    const lineData = {
        labels: ['January', 'February', 'March', 'April', 'May', 'June', 'July'],
        datasets: [
            {
                label: 'Sales',
                data: [65, 59, 80, 81, 56, 55, 40],
                fill: false,
                backgroundColor: 'rgba(75, 192, 192, 0.2)',
                borderColor: 'rgba(75, 192, 192, 1)',
            },
        ],
    };

    return (
        <div className="flex h-screen bg-gray-100 flex-col">
            <TopNavbar user={user} />
            <div className="flex flex-1">
                <aside className={`w-64 bg-white shadow-md ${open ? 'block' : 'hidden'} sm:block`}>
                    <div className="p-6">
                        <h1 className="text-2xl font-semibold text-gray-800">Dashboard</h1>
                        <nav className="mt-6">
<div className="flex items-center px-4 py-2 mt-5 text-gray-600 transition-colors duration-300 transform rounded-lg hover:bg-gray-200 hover:text-gray-700">
<HomeIcon className="w-6 h-6" />
<span className="mx-4">Home</span>
</div>
<div className="flex items-center px-4 py-2 mt-5 text-gray-600 transition-colors duration-300 transform rounded-lg hover:bg-gray-200 hover:text-gray-700">
<ChartBarIcon className="w-6 h-6" />
<span className="mx-4">Analytics</span>
</div>
<div className="flex items-center px-4 py-2 mt-5 text-gray-600 transition-colors duration-300 transform rounded-lg hover:bg-gray-200 hover:text-gray-700">
<ShoppingCartIcon className="w-6 h-6" />
<span className="mx-4">
<Link href="/portal/shows">Shows</Link>
</span>
</div>
<div className="flex items-center px-4 py-2 mt-5 text-gray-600 transition-colors duration-300 transform rounded-lg hover:bg-gray-200 hover:text-gray-700">
<ShoppingCartIcon className="w-6 h-6" />
<span className="mx-4">
<Link href="/shows">Tickets History</Link>
</span>
</div>
<div className="flex items-center px-4 py-2 mt-5 text-gray-600 transition-colors duration-300 transform rounded-lg hover:bg-gray-200 hover:text-gray-700">
<CameraIcon className="w-6 h-6" />
<span className="mx-4">
<Link href="/portal/shows">Scan Tickets</Link>
</span>
</div>
<div className="flex items-center px-4 py-2 mt-5 text-gray-600 transition-colors duration-300 transform rounded-lg hover:bg-gray-200 hover:text-gray-700">
<InboxInIcon className="w-6 h-6" />
<span className="mx-4">
<Link href="/shows">My Inbox</Link>
</span>
</div>
<div className="flex items-center px-4 py-2 mt-5 text-gray-600 transition-colors duration-300 transform rounded-lg hover:bg-gray-200 hover:text-gray-700">
<UserCircleIcon className="w-6 h-6" />
<span className="mx-4">User Profile</span>
</div>
<LogoutButton/>
</nav>
                    </div>
                </aside>
                <div className="flex-1 p-6">
                    {/* Mobile Menu Toggle Button */}
                    <button onClick={() => setOpen(!open)} className="text-gray-600 focus:outline-none sm:hidden">
                        <svg xmlns="http://www.w3.org/2000/svg" className="w-6 h-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M4 6h16M4 12h16M4 18h16" />
                        </svg>
                    </button>

                    {/* Dashboard Cards */}
                    <div className="grid grid-cols-1 gap-6 mt-6 lg:grid-cols-2 xl:grid-cols-3">
                        <div className="p-6 bg-white rounded-lg shadow-md">
                            <h2 className="text-lg font-semibold mb-4">Sales Overview</h2>
                            <Line data={lineData} />
                        </div>
                        <div className="p-6 bg-white rounded-lg shadow-md">
                            <h2 className="text-lg font-semibold mb-4">Votes Overview</h2>
                            <Doughnut data={doughnutData} />
                        </div>
                        <div className="p-6 bg-white rounded-lg shadow-md">
                            <h2 className="text-lg font-semibold mb-4">Other Metrics</h2>
                            <p className="mt-4 text-gray-600">Additional content or metrics can be displayed here.</p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    );
};

export default AdminDashboard;
