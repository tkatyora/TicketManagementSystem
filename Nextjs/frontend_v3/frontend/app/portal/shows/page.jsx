"use client"
import { useState, useEffect } from 'react';
import Link from 'next/link';
import { SearchIcon, FilterIcon, PlusIcon} from '@heroicons/react/outline';
import FetchShow from "@/app/componets/fetchShows"
import axios from 'axios';

const ShowsPage = () => {
  const [searchTerm, setSearchTerm] = useState('');
 
  const handleSearch = (e) => {
    const term = e.target.value;
    setSearchTerm(term);
    const filtered = shows.filter((show) =>
      show.showName.toLowerCase().includes(term.toLowerCase())
    );
    setFilteredShows(filtered);
  };

  const handleDelete = (id) => {
    axios.delete(`/api/shows/${id}`).then(() => {
      setFilteredShows(filteredShows.filter((show) => show.id !== id));
    });
  };

  return (
   
    <div className="container mx-auto px-4 py-6">
  
      <div className="flex justify-between items-center mb-4">
        <div className="flex items-center space-x-4">
          <div className="relative">
            <input
              type="text"
              value={searchTerm}
              onChange={handleSearch}
              placeholder="Search for shows"
              className="px-4 py-2 border border-gray-300 rounded-lg focus:outline-none"
            />
            <SearchIcon className="absolute top-2 right-2 w-6 h-6 text-gray-500" />
          </div>
          <button className="px-4 py-2 bg-blue-500 text-white rounded-lg hover:bg-blue-600 flex items-center">
            <FilterIcon className="w-6 h-6 mr-2" />
            Filter
          </button>
        </div>
        <Link href="/shows/add"
          className="px-4 py-2 bg-green-500 text-white rounded-lg hover:bg-green-600 flex items-center">
            <PlusIcon className="w-6 h-6 mr-2" />
            Add New Show
        
        </Link>
      </div>
      <FetchShow />
      
    </div>
  );
};

export default ShowsPage;
