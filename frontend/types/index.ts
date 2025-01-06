export interface LoginCredentials {
  email: string
  password: string
}

export interface SignupCredentials {
  email: string
  password: string
  full_name: string
  confirm_password?: string
}

export interface User {
  id: number
  email: string
  full_name: string
  is_active: boolean
  is_superuser: boolean
  created_at: string
  updated_at: string
}

export type UserUpdate = Partial<Omit<User, 'id' | 'created_at' | 'updated_at'>>

export interface Item {
  id: string
  title: string
  description?: string
  owner_id: string
}

export interface ItemsResponse {
  data: Item[]
  count: number
} 