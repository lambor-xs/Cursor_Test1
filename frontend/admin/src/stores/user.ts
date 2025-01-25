import { defineStore } from 'pinia'
import { ref } from 'vue'
import { login as loginApi } from '@/api/auth'
import type { LoginData } from '@/types/auth'

export const useUserStore = defineStore('user', () => {
  const token = ref(localStorage.getItem('token') || '')
  const isLoggedIn = ref(!!token.value)

  async function login(loginData: LoginData) {
    try {
      const response = await loginApi(loginData)
      token.value = response.access_token
      localStorage.setItem('token', token.value)
      isLoggedIn.value = true
    } catch (error) {
      console.error('登录失败:', error)
      throw error
    }
  }

  function logout() {
    token.value = ''
    localStorage.removeItem('token')
    isLoggedIn.value = false
  }

  return {
    token,
    isLoggedIn,
    login,
    logout
  }
}) 