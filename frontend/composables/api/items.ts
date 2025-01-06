import { useAxiosInstance } from './axiosInstance'
import type { Item } from '~/types'

interface ItemCreate {
  title: string
  description?: string
}

interface ItemUpdate {
  title?: string
  description?: string
}

interface ItemsResponse {
  data: Item[]
  count: number
}

export const itemsApi = {
  // Get all items with pagination
  getItems: async (skip: number = 0, limit: number = 100): Promise<ItemsResponse> => {
    const axios = useAxiosInstance()
    const response = await axios.get(`/api/v1/items/?skip=${skip}&limit=${limit}`)
    return response.data
  },

  // Get a single item by ID
  getItem: async (id: string): Promise<Item> => {
    const axios = useAxiosInstance()
    const response = await axios.get(`/api/v1/items/${id}`)
    return response.data
  },

  // Create a new item
  createItem: async (item: ItemCreate): Promise<Item> => {
    const axios = useAxiosInstance()
    const response = await axios.post('/api/v1/items/', item)
    return response.data
  },

  // Update an existing item
  updateItem: async (id: string, item: ItemUpdate): Promise<Item> => {
    const axios = useAxiosInstance()
    const response = await axios.put(`/api/v1/items/${id}`, item)
    return response.data
  },

  // Delete an item
  deleteItem: async (id: string): Promise<{ message: string }> => {
    const axios = useAxiosInstance()
    const response = await axios.delete(`/api/v1/items/${id}`)
    return response.data
  }
} 