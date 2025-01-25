import request from '@/utils/request'
import type { LoginData, LoginResponse, RegisterData, User } from '@/types/auth'

export function login(data: LoginData) {
  const formData = new FormData()
  formData.append('username', data.username)
  formData.append('password', data.password)
  
  return request.post<LoginResponse>('/login/access-token', formData, {
    headers: {
      'Content-Type': 'multipart/form-data'
    }
  })
}

export function register(data: RegisterData) {
  return request.post<User>('/register', data)
}

export function getUserInfo() {
  return request.get<User>('/me')
} 