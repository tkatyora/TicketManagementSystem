import React from 'react';

const Modal = ({ showModal, onClose, onConfirm, showName }) => {
  if (!showModal) return null;

  return (
    <div className="fixed inset-0 flex items-center justify-center z-50">
      <div className="fixed inset-0 bg-black opacity-50" onClick={onClose} />
      <div className="bg-white p-6 rounded-lg shadow-lg z-10">
        <h2 className="text-lg font-bold mb-4">Confirm Delete</h2>
        <p className="mb-4">Are you sure you want to delete {showName}'s Show?</p>
        <div className="flex justify-end space-x-4">
          <button
            onClick={onClose}
            className="px-4 py-2 bg-gray-300 text-gray-700 rounded-lg"
          >
            No
          </button>
          <button
            onClick={onConfirm}
            className="px-4 py-2 bg-red-500 text-white rounded-lg"
          >
            Delete
          </button>
        </div>
      </div>
    </div>
  );
};

export default Modal;
