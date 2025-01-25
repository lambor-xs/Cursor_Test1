/**
 * Vite 项目配置文件
 * 用于配置项目的构建、开发服务器等选项
 */

import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import * as path from 'path'
import { fileURLToPath } from 'url'

const __dirname = path.dirname(fileURLToPath(import.meta.url))

export default defineConfig({
  // 插件配置
  plugins: [
    vue()  // 启用 Vue 3 支持
  ],
  
  // 路径解析配置
  resolve: {
    alias: {
      '@': path.resolve(__dirname, 'src'),  // 设置 @ 指向 src 目录
    },
  },
  
  // 开发服务器配置
  server: {
    port: 3000,  // 开发服务器端口
    proxy: {
      // 代理配置
      '/api': {
        target: 'http://localhost:8000',  // 后端服务地址
        changeOrigin: true,  // 支持跨域
      },
    },
  },
}) 