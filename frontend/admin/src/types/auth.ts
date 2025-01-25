export interface LoginData {
  username: string
  password: string
}

export interface RegisterData {
  username: string
  email: string
  password: string
}

export interface LoginResponse {
  access_token: string
  token_type: string
}

export interface User {
  id: number
  email: string
  username: string
  is_active: boolean
  is_admin: boolean
  created_at: string
  updated_at: string | null
} 