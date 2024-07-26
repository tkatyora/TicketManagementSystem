import React, { useState } from 'react';

const GenerateTickets = ({ showModal, onClose, onConfirm, showName }) => {
  const [customerName, setCustomerName] = useState('');
  const [numberPeople, setNumberPeople] = useState(1);

  if (!showModal) return null;

  const handleConfirm = () => {
    onConfirm(customerName, numberPeople);
  };

  return (
    <div className="fixed inset-0 flex items-center justify-center z-50">
      <div className="fixed inset-0 bg-black opacity-50" onClick={onClose} />
      <div className="bg-white p-6 rounded-lg shadow-lg z-10">
        <h2 className="text-lg font-bold mb-4">Generate Ticket for {showName}</h2>
        <div className="mb-4">
          <label className="block text-gray-700">Customer Name</label>
          <input
            type="text"
            value={customerName}
            onChange={(e) => setCustomerName(e.target.value)}
            className="w-full px-3 py-2 border border-gray-300 rounded-lg"
          />
        </div>
        <div className="mb-4">
          <label className="block text-gray-700">Number of Tickets</label>
          <input
            type="number"
            value={numberPeople}
            onChange={(e) => setNumberPeople(e.target.value)}
            className="w-full px-3 py-2 border border-gray-300 rounded-lg"
            min="1"
          />
        </div>
        <div className="flex justify-end space-x-4">
          <button
            onClick={onClose}
            className="px-4 py-2 bg-gray-300 text-gray-700 rounded-lg"
          >
            Cancel
          </button>
          <button
            onClick={handleConfirm}
            className="px-4 py-2 bg-yellow-500 text-white rounded-lg"
          >
            Generate
          </button>
        </div>
      </div>
    </div>
  );
};

export default GenerateTickets;
