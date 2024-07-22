"use client"
import React from 'react'
import { useEffect , useState } from 'react';
import { getAllShow } from '../ApiServices/showApi';
import Link from 'next/link';
import { PencilAltIcon,TrashIcon, EyeIcon } from '@heroicons/react/outline';


const FetchShows = () => {
    const [shows, setShow] = useState([]);
    const [filteredShows, setFilteredShows] = useState([]);
    console.log('data being fetched')
    console.log(shows)
  
    useEffect(() => {
    getAllShow()
      .then(data => setShow(data))
      .catch(error => {
        console.error('There was an error fetching the products!', error);
      });
     
  }, []);

  return (
    <>
    <table className="min-w-full bg-white">
        <thead>
          <tr>
            <th className="py-2 px-4 border-b">Show Name</th>
            <th className="py-2 px-4 border-b">Venue</th>
            <th className="py-2 px-4 border-b">City</th>
            <th className="py-2 px-4 border-b">Date</th>
            <th className="py-2 px-4 border-b">Actions</th>
          </tr>
        </thead>
        <tbody>
          {shows.map((show) => (
            <tr key={show.id}>
              <td className="py-2 px-4 border-b">{show.showName}</td>
              <td className="py-2 px-4 border-b">{show.showVenue}</td>
              <td className="py-2 px-4 border-b">{show.showCity}</td>
              <td className="py-2 px-4 border-b">{show.showDate}</td>
              <td className="py-2 px-4 border-b flex space-x-2">
                <Link href={`/shows/${show.id}`} className="text-blue-500 hover:text-blue-700">
                    <EyeIcon className="w-5 h-5" />
                 
                </Link>
                <Link href={`/shows/edit/${show.id}`}
              className="text-green-500 hover:text-green-700">
                    <PencilAltIcon className="w-5 h-5" />
                 
                </Link>
                <button onClick={() => handleDelete(show.id)} className="text-red-500 hover:text-red-700">
                  <TrashIcon className="w-5 h-5" />
                </button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </>
  )
}

export default FetchShows