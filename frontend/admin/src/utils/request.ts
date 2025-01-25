import axios from 'axios'
import { ElMessage } from 'element-plus'
import router from '@/router'

const request = axios.create({
  baseURL: '/api/v1',
  timeout: 5000
})

// 请求拦截器
request.interceptors.request.use(
  config => {
    const token = localStorage.getItem('token')
    if (token) {
      config.headers.Authorization = `Bearer ${token}`
    }
    return config
  },
  error => {
    ElMessage.error('请求发送失败')
    return Promise.reject(error)
  }
)

// 响应拦截器
request.interceptors.response.use(
  response => {
    // 直接返回响应数据
    return response.data
  },
  error => {
    let errorMessage = '操作失败'
    
    if (error.response) {
      const status = error.response.status
      const detail = error.response.data?.detail
      
      if (detail) {
        errorMessage = detail
      } else if (status === 401) {
        errorMessage = '登录已过期，请重新登录'
        localStorage.removeItem('token')
        router.push('/login')
      } else if (status === 403) {
        errorMessage = '没有权限访问'
      } else if (status === 404) {
        errorMessage = '请求的资源不存在'
      } else if (status === 500) {
        errorMessage = '服务器内部错误'
      }
    } else if (!navigator.onLine) {
      errorMessage = '网络连接失败，请检查网络'
    }

    ElMessage.error(errorMessage)
    return Promise.reject(error)
  }
)

export default request 