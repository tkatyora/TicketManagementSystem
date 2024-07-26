"use client"
import React from 'react'
import { TicketIcon} from '@heroicons/react/outline';
import { useState } from 'react';
import GenerateTickets from "@/app/Form/generateTicket";
import axiosInstance from '../ApiServices/axiosConfig';



const GenerateTicketComponet = (show) => {

    const [selectedShow, setSelectedShow] = useState(null);
    const [showModal, setShowModal] = useState(false);


    const handleGenerateClick = (show) => {
        setSelectedShow(show);
        setShowModal(true);
      };

  const handleCloseModal = () => {
    setShowModal(false);
  };


  const handleConfirmGenerate = (customerName, numberPeople) => {
    if (selectedShow) {
      const data = {
        show_details: selectedShow.id,
        customerName: customerName,
        numberPeople: numberPeople,
        amountPaid : 24
        // amountPaid: numberPeople * selectedShow.ticketPrice 
      };

      axiosInstance.post('/tickets_api/create/', data)
        .then(response => {
          console.log('Ticket created successfully:', response.data);
          // Handle success, maybe show a success message or update the state
        })
        .catch(error => {
          console.error('Error creating ticket:', error);
          // Handle error, maybe show an error message
        })
        .finally(() => {
          handleCloseModal();
        });
    }
  };
 

  return (
    <div>
        <button
                  onClick={() => handleGenerateClick(show)}
                  className="text-yellow-500 hover:text-blue-700"
                >
                  <TicketIcon className="w-5 h-5 cursor-pointer" />
                </button>


                <GenerateTickets
        showModal={showModal}
        onClose={handleCloseModal}
        onConfirm={handleConfirmGenerate}
        showName={selectedShow ? selectedShow.showName : ''}
      />

    </div>
  )
}

export default GenerateTicketComponet