"use client"
import React, { useEffect, useState } from 'react';
import { getAllShow, deleteProduct } from '../ApiServices/showApi';
import Link from 'next/link';
import { PencilAltIcon, TrashIcon, EyeIcon ,TicketIcon} from '@heroicons/react/outline';
import Modal from "@/app/componets/modal"
import toast from 'react-hot-toast';
import GenerateTicketComponet from "@/app/componets/generateTicketComponet";


const FetchShows = () => {
  const [shows, setShows] = useState([]);
  const [showModal, setShowModal] = useState(false);
  const [showToDelete, setShowToDelete] = useState(null);
  const [error , setError] = useState('')
 



  useEffect(() => {
    getAllShow()
      .then(data => setShows(data))
      .catch(error => {
        toast.error('There was an error fetching the shows!');
        console.error('There was an error fetching the shows!', error);
        setError('There was an error fetching the shows!')
      });
  }, []);

  const handleDeleteClick = (show) => {
    setShowToDelete(show);
    setShowModal(true);
  };

  const handleConfirmDelete = async () => {
    if (showToDelete) {
      try {
        await deleteProduct(showToDelete.id);
        toast.success(`Show "${showToDelete.showName}" deleted successfully!`);
        setShows(shows.filter(show => show.id !== showToDelete.id));
        setShowModal(false);
      } catch (error) {
        console.error('There was an error deleting the show!', error);
        toast.error('There was an error deleting the show.');
        setShowModal(false);
      }
    }
  };

  const handleCloseModal = () => {
    setShowModal(false);
    setShowToDelete(null);
  };



  return (
    <div className="container mx-auto p-4">
       {error && <div className="text-red-500 mb-4">{error}</div>} 
      <div className="overflow-x-auto">
        <table className="min-w-full bg-white shadow-md rounded-lg">
          <thead>
            <tr className="bg-gray-800 text-white">
              <th className="py-3 px-4">Show Name</th>
              <th className="py-3 px-4">Venue</th>
              <th className="py-3 px-4">City</th>
              <th className="py-3 px-4">Date</th>
              <th className="py-3 px-4">No Tickets</th>
              <th className="py-3 px-4">Tickets Left</th>
              <th className="py-3 px-4">Tickets Boughts</th>
              <th className="py-3 px-4">Actions</th>
            </tr>
          </thead>
          <tbody>
            {shows.map((show) => (
              <tr key={show.id} className="hover:bg-gray-100 even:bg-gray-50">
                <td className="py-3 px-4 border-b">{show.showName}</td>
                <td className="py-3 px-4 border-b">{show.showVenue}</td>
                <td className="py-3 px-4 border-b">{show.showCity}</td>
                <td className="py-3 px-4 border-b">{show.showDate}</td>
                <td className="py-3 px-4 border-b">{show.numbertickets}</td>
                <td className="py-3 px-4 border-b">${show.vvip_price}</td>
                <td className="py-3 px-4 border-b">${show.vvip_price}</td>
          
                <td className="py-3 px-4 border-b flex space-x-2">
                 <GenerateTicketComponet 
                 show={show}/>
                  <Link href={`/shows/${show.id}`} className="text-blue-500 hover:text-blue-700">
                    <EyeIcon className="w-5 h-5 cursor-pointer" />
                  </Link>
                  <Link href={`/shows/edit/${show.id}`} className="text-green-500 hover:text-green-700">
                    <PencilAltIcon className="w-5 h-5 cursor-pointer" />
                  </Link>
                  <button onClick={() => handleDeleteClick(show)} className="text-red-500 hover:text-red-700">
                    <TrashIcon className="w-5 h-5 cursor-pointer" />
                  </button>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
      <Modal
        showModal={showModal}
        onClose={handleCloseModal}
        onConfirm={handleConfirmDelete}
        showName={showToDelete ? showToDelete.showName : ''}
      />
       
    </div>
  );
};

export default FetchShows;
