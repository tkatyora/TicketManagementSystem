import axiosInstance from './axiosConfig';

const LogIn = async (usernameOrEmail, password) => {
  try {
    const response = await axiosInstance.post('/auth_api/login/', {
      username_or_email: usernameOrEmail,
      password: password,
    });
    return response.data;
  } catch (error) {
    throw error;
  }
};

export default LogIn;






