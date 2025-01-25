/**
 * Vite 环境变量类型声明文件
 * 用于定义环境变量的类型，提供类型检查和代码提示
 */

/// <reference types="vite/client" />

/**
 * 环境变量接口
 * 定义了所有可用的环境变量及其类型
 */
interface ImportMetaEnv {
  /** API基础路径 */
  readonly VITE_API_URL: string
  /** 应用标题 */
  readonly VITE_APP_TITLE: string
}

/**
 * ImportMeta接口扩展
 * 为import.meta添加env属性的类型
 */
interface ImportMeta {
  readonly env: ImportMetaEnv
} 