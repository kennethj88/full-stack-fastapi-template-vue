import { useAxiosInstance } from './axiosInstance'
import type { LoginCredentials, SignupCredentials, User } from '~/types'

export const authApi = {
  login: async (credentials: LoginCredentials) => {
    const formData = new FormData()
    formData.append('username', credentials.email)
    formData.append('password', credentials.password)
    
    const { data } = await useAxiosInstance().post(
      'api/v1/auth/login/access-token',
      formData,
      {
        headers: {
          'Content-Type': 'application/x-www-form-urlencoded'
        }
      }
    )
    return data
  },

  signup: async (credentials: SignupCredentials) => {
    const axios = useAxiosInstance()
    const response = await axios.post('/api/v1/users/signup', credentials)
    return response.data
  },

  forgotPassword: async (email: string) => {
    const axios = useAxiosInstance()
    const response = await axios.post(`/api/v1/password-recovery/${email}`)
    return response.data
  },

  resetPassword: async (token: string, newPassword: string) => {
    const axios = useAxiosInstance()
    const response = await axios.post('/api/v1/reset-password/', {
      token,
      new_password: newPassword
    })
    return response.data
  },

  getCurrentUser: async (): Promise<User> => {
    const axios = useAxiosInstance()
    const response = await axios.get('/api/v1/users/me')
    return response.data
  },

  updateProfile: async (userData: Partial<User>) => {
    const axios = useAxiosInstance()
    const response = await axios.patch('/api/v1/users/me', userData)
    return response.data
  },

  updatePassword: async (currentPassword: string, newPassword: string) => {
    const axios = useAxiosInstance()
    const response = await axios.patch('/api/v1/users/me/password', {
      current_password: currentPassword,
      new_password: newPassword
    })
    return response.data
  },

  async googleLogin(token: string) {
    const { data } = await useAxiosInstance().post('/api/v1/auth/google', { token })
    return data
  },
  
  async linkGoogleAccount(token: string, password: string) {
    const { data } = await useAxiosInstance().post('/api/v1/auth/google/link', {
      token,
      password
    })
    return data
  }
} 