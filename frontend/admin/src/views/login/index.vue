<template>
  <div class="login-container">
    <el-card class="login-card">
      <template #header>
        <h2 class="login-title">{{ title }}</h2>
      </template>
      <el-form
        ref="formRef"
        :model="form"
        :rules="rules"
        label-position="top"
        @keyup.enter="handleSubmit"
      >
        <el-form-item label="用户名" prop="username">
          <el-input
            v-model="form.username"
            placeholder="请输入用户名"
            :prefix-icon="User"
          />
        </el-form-item>
        <el-form-item
          v-if="isRegister"
          label="邮箱"
          prop="email"
        >
          <el-input
            v-model="form.email"
            placeholder="请输入邮箱"
            :prefix-icon="Message"
          />
        </el-form-item>
        <el-form-item label="密码" prop="password">
          <el-input
            v-model="form.password"
            type="password"
            placeholder="请输入密码"
            :prefix-icon="Lock"
            show-password
          />
        </el-form-item>
        <el-form-item>
          <el-button
            type="primary"
            class="submit-button"
            :loading="loading"
            @click="handleSubmit"
          >
            {{ isRegister ? '注册' : '登录' }}
          </el-button>
        </el-form-item>
      </el-form>
      <div class="form-footer">
        <el-button
          link
          type="primary"
          @click="toggleMode"
        >
          {{ isRegister ? '已有账号？去登录' : '没有账号？去注册' }}
        </el-button>
      </div>
    </el-card>
  </div>
</template>

<script setup lang="ts">
import { ref, computed } from 'vue'
import { useRouter } from 'vue-router'
import { ElMessage } from 'element-plus'
import type { FormInstance, FormRules } from 'element-plus'
import { User, Lock, Message } from '@element-plus/icons-vue'
import { useUserStore } from '@/stores/user'
import { register } from '@/api/auth'
import type { LoginData, RegisterData } from '@/types/auth'

const title = import.meta.env.VITE_APP_TITLE
const router = useRouter()
const userStore = useUserStore()
const formRef = ref<FormInstance>()
const loading = ref(false)
const isRegister = ref(false)

const form = ref({
  username: '',
  email: '',
  password: ''
})

const rules = computed<FormRules>(() => ({
  username: [
    { required: true, message: '请输入用户名', trigger: 'blur' },
    { min: 3, message: '用户名长度不能小于3个字符', trigger: 'blur' }
  ],
  email: isRegister.value ? [
    { required: true, message: '请输入邮箱地址', trigger: 'blur' },
    { type: 'email', message: '请输入正确的邮箱地址', trigger: 'blur' }
  ] : [],
  password: [
    { required: true, message: '请输入密码', trigger: 'blur' },
    { min: 6, message: '密码长度不能小于6个字符', trigger: 'blur' }
  ]
}))

const toggleMode = () => {
  isRegister.value = !isRegister.value
  form.value = {
    username: '',
    email: '',
    password: ''
  }
}

const handleSubmit = async () => {
  if (!formRef.value) return
  
  try {
    await formRef.value.validate()
    loading.value = true
    
    if (isRegister.value) {
      await register(form.value as RegisterData)
      ElMessage.success('注册成功')
      isRegister.value = false
      form.value = {
        username: '',
        email: '',
        password: ''
      }
    } else {
      await userStore.login(form.value as LoginData)
      ElMessage.success('登录成功')
      router.push('/')
    }
  } catch (error: any) {
    console.error('操作失败:', error)
    // 不再显示错误消息，因为已经在请求拦截器中处理了
  } finally {
    loading.value = false
  }
}
</script>

<style lang="scss" scoped>
.login-container {
  height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
}

.login-card {
  width: 100%;
  max-width: 400px;
  margin: 0 20px;
  border-radius: 8px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

.login-title {
  margin: 0;
  text-align: center;
  color: #333;
  font-size: 24px;
}

.submit-button {
  width: 100%;
  padding: 12px;
  font-size: 16px;
}

.form-footer {
  text-align: center;
  margin-top: 16px;
}

:deep(.el-input__wrapper) {
  padding: 0 11px;
}

:deep(.el-input__prefix) {
  margin-right: 8px;
}
</style> 