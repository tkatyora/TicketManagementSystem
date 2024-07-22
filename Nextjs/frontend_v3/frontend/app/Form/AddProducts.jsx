"use client"
import { useEffect , useState } from 'react';
import { createProduct } from '../ApiServices/showApi';
import axios from 'axios';
import { useRouter } from 'next/navigation';

const AddProduct = () => {
  const [formData, setFormData] = useState({
    picture: null,
    showName: '',
    showVenue: '',
    showCity: '',
    showDate: '',
    vip_price: '',
    vvip_price: '',
    general_price: '',
    numbertickets: ''
  });

  const cities = [
    { id: 1, name: 'Harare' },
    { id: 2, name: 'Mutare' },
    { id: 3, name: 'Bulawayo' },
    { id: 4, name: 'Chitungwiza' },
    { id: 5, name: 'Gweru' },
    { id: 6, name: 'Masvingo' },
    { id: 7, name: 'Kadoma' },
    { id: 8, name: 'Kwekwe' },
    { id: 9, name: 'Chinhoyi' },
    { id: 10, name: 'Norton' }
  ];

  const router = useRouter();

  const handleChange = (e) => {
    const { name, value, files } = e.target;
    if (name === 'picture') {
      setFormData({
        ...formData,
        [name]: files[0]
      });
    } else {
      setFormData({
        ...formData,
        [name]: value
      });
    }
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    const formDataToSend = new FormData();
    for (const key in formData) {
      formDataToSend.append(key, formData[key]);
    }
    console.log(Array.from(formDataToSend.entries())); 
    try {
      const response = await createProduct(formDataToSend);
      console.log(response);
      router.push('/shows');
    } catch (error) {
      if (error.response) {
        console.error("Error response data:", error.response.data);
      } else {
        console.error("Error:", error.message);
      }
    }
  };


  return (
    <div className="flex items-center justify-center">
      <div className="bg-white p-6 rounded-lg shadow-lg w-full max-w-md mt-7 mb-7">
        <h2 className="text-2xl font-bold mb-4 text-center">Add New Show</h2>
        <form onSubmit={handleSubmit} encType="multipart/form-data">
          <div className="mb-4">
            <label className="block text-gray-700">Picture</label>
            <input
              type="file"
              name="picture"
              onChange={handleChange}
              className="mt-1 block w-full p-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-600"
            />
          </div>
          <div className="mb-4">
            <label className="block text-gray-700">Show Name<span className="text-red-500">*</span></label>
            <input
              type="text"
              name="showName"
              value={formData.showName}
              onChange={handleChange}
              className="mt-1 block w-full p-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-600"
              required
            />
          </div>
          <div className="mb-4">
            <label className="block text-gray-700">Show Venue<span className="text-red-500">*</span></label>
            <input
              type="text"
              name="showVenue"
              value={formData.showVenue}
              onChange={handleChange}
              className="mt-1 block w-full p-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-600"
              required
            />
          </div>
          <div className="mb-4">
            <label className="block text-gray-700">Show City<span className="text-red-500">*</span></label>
            <select
              name="showCity"
              value={formData.showCity}
              onChange={handleChange}
              className="mt-1 block w-full p-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-600"
              required
            >
              <option value="">Select a city</option>
              {cities.map(city => (
                <option key={city.id} value={city.name}>
                  {city.name}
                </option>
              ))}
            </select>
          </div>
          <div className="mb-4">
            <label className="block text-gray-700">Show Date<span className="text-red-500">*</span></label>
            <input
              type="date"
              name="showDate"
              value={formData.showDate}
              onChange={handleChange}
              className="mt-1 block w-full p-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-600"
              required
            />
          </div>
          <div className="mb-4">
            <label className="block text-gray-700">VIP Price</label>
            <input
              type="number"
              name="vip_price"
              value={formData.vip_price}
              onChange={handleChange}
              className="mt-1 block w-full p-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-600"
              required
            />
          </div>
          <div className="mb-4">
            <label className="block text-gray-700">VVIP Price</label>
            <input
              type="number"
              name="vvip_price"
              value={formData.vvip_price}
              onChange={handleChange}
              className="mt-1 block w-full p-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-600"
              required
            />
          </div>
          <div className="mb-4">
            <label className="block text-gray-700">General Price</label>
            <input
              type="number"
              name="general_price"
              value={formData.general_price}
              onChange={handleChange}
              className="mt-1 block w-full p-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-600"
              required
            />
          </div>
          <div className="mb-4">
            <label className="block text-gray-700">Number of Tickets <span className="text-red-500">*</span></label>
            <input
              type="number"
              name="numbertickets"
              value={formData.numbertickets}
              onChange={handleChange}
              className="mt-1 block w-full p-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-600"
              required
            />
          </div>
          <div className="flex justify-center">
            <button
              type="submit"
              className="bg-blue-600 text-white px-4 py-2 rounded-lg hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-blue-600"
            >
              Add Show
            </button>
          </div>
        </form>
      </div>
    </div>
  );
};

export default AddProduct;
