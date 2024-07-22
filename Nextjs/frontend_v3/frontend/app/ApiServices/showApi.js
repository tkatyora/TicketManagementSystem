import axiosInstance from './axiosConfig';

export const getAllShow = async () => {
  try {
    const response = await axiosInstance.get('/shows_api/shows/');
    return response.data;
  } catch (error) {
    throw error;
  }
};

export const getProductById = async (id) => {
  try {
    const response = await axiosInstance.get(`/shows_api/shows/${id}/`);
    return response.data;
  } catch (error) {
    throw error;
  }
};

export const createProduct = async (showData) => {
  try {
    const response = await axiosInstance.post('/shows_api/shows/', showData);
    return response.data;
  } catch (error) {
    throw error;
  }
};


export const updateProduct = async (id, showDataData) => {
  try {
    const response = await axiosInstance.patch(`/shows_api/shows/`, showData);
    return response.data;
  } catch (error) {
    throw error;
  }
};
export const deleteProduct = async (id) => {
  try {
    const response = await axiosInstance.delete(`/shows_api/shows/${id}/`);
    return response.data;
  } catch (error) {
    throw error;
  }
};