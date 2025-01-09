//composables/api/axiosInstance.ts
import axios from 'axios';

export const useAxiosInstance = () => {
  const config = useRuntimeConfig();
  
  const instance = axios.create({
    baseURL: config.public.apiUrl,
    timeout: 10000,
  });

  // Add request interceptor for debugging
  instance.interceptors.request.use((config) => {
    console.log('API Request:', {
      method: config.method,
      url: config.url,
      data: config.data,
      headers: config.headers
    })
    return config
  })

  // Add response interceptor for debugging
  instance.interceptors.response.use(
    (response) => {
      console.log('API Response:', {
        status: response.status,
        data: response.data
      })
      return response
    },
    (error) => {
      console.error('API Error:', {
        status: error.response?.status,
        data: error.response?.data,
        message: error.message
      })
      return Promise.reject(error)
    }
  )

  return instance;
};