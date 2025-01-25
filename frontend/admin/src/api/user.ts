import request from '@/utils/request'
import type { User } from '@/types/auth'

export interface UserListParams {
  page?: number
  limit?: number
  search?: string
}

export interface UserListResponse {
  data: User[]
  total: number
}

export function getUserList(params: UserListParams) {
  return request.get<UserListResponse>('/api/v1/users', { params })
}

export function getUser(id: number) {
  return request.get<User>(`/api/v1/users/${id}`)
}

export function createUser(data: Partial<User>) {
  return request.post<User>('/api/v1/users', data)
}

export function updateUser(id: number, data: Partial<User>) {
  return request.put<User>(`/api/v1/users/${id}`, data)
}

export function deleteUser(id: number) {
  return request.delete<User>(`/api/v1/users/${id}`)
} 