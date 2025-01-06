//composables/api/axiosInstance.ts
import axios from 'axios';

export const useAxiosInstance = () => {
  const config = useRuntimeConfig();
  
  const instance = axios.create({
    baseURL: config.public.apiUrl || 'http://localhost:8000',
    headers: {
      'Content-Type': 'application/json'
    }
  });

  // Add request interceptor to add auth token
  instance.interceptors.request.use(
    (config) => {
      const token = useCookie('access_token').value;
      if (token) {
        config.headers.Authorization = `Bearer ${token}`;
      }
      return config;
    },
    (error) => {
      return Promise.reject(error);
    }
  );

  // Add response interceptor to handle errors
  instance.interceptors.response.use(
    (response) => response,
    async (error) => {
      console.log('API Reqeust error:', error.response?.status)
      if (error.response?.status === 401) {
        // Handle unauthorized access
        const auth = useAuthStore();
        //await auth.logout();
        //navigateTo('/login');
      }
      return Promise.reject(error);
    }
  );

  return instance;
};