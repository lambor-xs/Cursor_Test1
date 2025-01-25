<template>
  <div class="users-container">
    <el-card>
      <template #header>
        <div class="card-header">
          <div class="left">
            <el-input
              v-model="searchQuery"
              placeholder="搜索用户..."
              class="search-input"
              clearable
              @clear="handleSearch"
              @keyup.enter="handleSearch"
            >
              <template #prefix>
                <el-icon><Search /></el-icon>
              </template>
            </el-input>
          </div>
          <div class="right">
            <el-button type="primary" @click="handleAdd">
              <el-icon><Plus /></el-icon>添加用户
            </el-button>
          </div>
        </div>
      </template>

      <el-table
        v-loading="loading"
        :data="users"
        style="width: 100%"
        border
      >
        <el-table-column prop="id" label="ID" width="80" />
        <el-table-column prop="username" label="用户名" />
        <el-table-column prop="email" label="邮箱" />
        <el-table-column prop="is_active" label="状态" width="100">
          <template #default="{ row }">
            <el-tag :type="row.is_active ? 'success' : 'danger'">
              {{ row.is_active ? '启用' : '禁用' }}
            </el-tag>
          </template>
        </el-table-column>
        <el-table-column prop="is_admin" label="角色" width="100">
          <template #default="{ row }">
            <el-tag :type="row.is_admin ? 'warning' : 'info'">
              {{ row.is_admin ? '管理员' : '普通用户' }}
            </el-tag>
          </template>
        </el-table-column>
        <el-table-column prop="created_at" label="创建时间" width="180">
          <template #default="{ row }">
            {{ formatDate(row.created_at) }}
          </template>
        </el-table-column>
        <el-table-column label="操作" width="200" fixed="right">
          <template #default="{ row }">
            <el-button-group>
              <el-button type="primary" @click="handleEdit(row)">
                编辑
              </el-button>
              <el-button
                type="danger"
                @click="handleDelete(row)"
              >
                删除
              </el-button>
            </el-button-group>
          </template>
        </el-table-column>
      </el-table>

      <div class="pagination-container">
        <el-pagination
          v-model:current-page="currentPage"
          v-model:page-size="pageSize"
          :page-sizes="[10, 20, 50, 100]"
          :total="total"
          layout="total, sizes, prev, pager, next, jumper"
          @size-change="handleSizeChange"
          @current-change="handleCurrentChange"
        />
      </div>
    </el-card>

    <!-- 用户表单对话框 -->
    <el-dialog
      v-model="dialogVisible"
      :title="dialogType === 'add' ? '添加用户' : '编辑用户'"
      width="500px"
    >
      <el-form
        ref="formRef"
        :model="form"
        :rules="rules"
        label-width="80px"
      >
        <el-form-item label="用户名" prop="username">
          <el-input v-model="form.username" />
        </el-form-item>
        <el-form-item label="邮箱" prop="email">
          <el-input v-model="form.email" />
        </el-form-item>
        <el-form-item
          label="密码"
          prop="password"
          :rules="dialogType === 'add' ? rules.password : []"
        >
          <el-input
            v-model="form.password"
            type="password"
            placeholder="留空表示不修改密码"
          />
        </el-form-item>
        <el-form-item label="状态">
          <el-switch v-model="form.is_active" />
        </el-form-item>
        <el-form-item label="角色">
          <el-switch
            v-model="form.is_admin"
            active-text="管理员"
            inactive-text="普通用户"
          />
        </el-form-item>
      </el-form>
      <template #footer>
        <span class="dialog-footer">
          <el-button @click="dialogVisible = false">取消</el-button>
          <el-button type="primary" @click="handleSubmit">
            确定
          </el-button>
        </span>
      </template>
    </el-dialog>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { ElMessage, ElMessageBox } from 'element-plus'
import { Search, Plus } from '@element-plus/icons-vue'
import type { FormInstance } from 'element-plus'
import type { User } from '@/types/auth'

const loading = ref(false)
const users = ref<User[]>([])
const total = ref(0)
const currentPage = ref(1)
const pageSize = ref(10)
const searchQuery = ref('')
const dialogVisible = ref(false)
const dialogType = ref<'add' | 'edit'>('add')
const formRef = ref<FormInstance>()

const form = ref({
  id: 0,
  username: '',
  email: '',
  password: '',
  is_active: true,
  is_admin: false
})

const rules = {
  username: [
    { required: true, message: '请输入用户名', trigger: 'blur' },
    { min: 3, message: '用户名长度不能小于3个字符', trigger: 'blur' }
  ],
  email: [
    { required: true, message: '请输入邮箱地址', trigger: 'blur' },
    { type: 'email', message: '请输入正确的邮箱地址', trigger: 'blur' }
  ],
  password: [
    { required: true, message: '请输入密码', trigger: 'blur' },
    { min: 6, message: '密码长度不能小于6个字符', trigger: 'blur' }
  ]
}

const formatDate = (date: string) => {
  return new Date(date).toLocaleString()
}

const fetchUsers = async () => {
  loading.value = true
  try {
    // TODO: 实现用户列表获取API
    // const response = await getUserList({
    //   page: currentPage.value,
    //   limit: pageSize.value,
    //   search: searchQuery.value
    // })
    // users.value = response.data
    // total.value = response.total

    // 模拟数据
    users.value = [
      {
        id: 1,
        username: 'admin',
        email: 'admin@example.com',
        is_active: true,
        is_admin: true,
        created_at: new Date().toISOString(),
        updated_at: null
      }
    ]
    total.value = 1
  } catch (error) {
    console.error('Failed to fetch users:', error)
    ElMessage.error('获取用户列表失败')
  } finally {
    loading.value = false
  }
}

const handleSearch = () => {
  currentPage.value = 1
  fetchUsers()
}

const handleSizeChange = (val: number) => {
  pageSize.value = val
  fetchUsers()
}

const handleCurrentChange = (val: number) => {
  currentPage.value = val
  fetchUsers()
}

const resetForm = () => {
  form.value = {
    id: 0,
    username: '',
    email: '',
    password: '',
    is_active: true,
    is_admin: false
  }
}

const handleAdd = () => {
  dialogType.value = 'add'
  resetForm()
  dialogVisible.value = true
}

const handleEdit = (row: User) => {
  dialogType.value = 'edit'
  form.value = {
    ...row,
    password: ''
  }
  dialogVisible.value = true
}

const handleDelete = (row: User) => {
  ElMessageBox.confirm(
    '确定要删除该用户吗？',
    '警告',
    {
      confirmButtonText: '确定',
      cancelButtonText: '取消',
      type: 'warning'
    }
  ).then(async () => {
    try {
      // TODO: 实现删除用户API
      // await deleteUser(row.id)
      ElMessage.success('删除成功')
      fetchUsers()
    } catch (error) {
      console.error('Failed to delete user:', error)
      ElMessage.error('删除失败')
    }
  })
}

const handleSubmit = async () => {
  if (!formRef.value) return

  await formRef.value.validate(async (valid) => {
    if (valid) {
      try {
        // TODO: 实现添加/编辑用户API
        // if (dialogType.value === 'add') {
        //   await createUser(form.value)
        // } else {
        //   await updateUser(form.value.id, form.value)
        // }
        ElMessage.success(
          dialogType.value === 'add' ? '添加成功' : '编辑成功'
        )
        dialogVisible.value = false
        fetchUsers()
      } catch (error) {
        console.error('Failed to submit form:', error)
        ElMessage.error(
          dialogType.value === 'add' ? '添加失败' : '编辑失败'
        )
      }
    }
  })
}

onMounted(() => {
  fetchUsers()
})
</script>

<style lang="scss" scoped>
.users-container {
  .card-header {
    display: flex;
    justify-content: space-between;
    align-items: center;

    .search-input {
      width: 300px;
    }
  }

  .pagination-container {
    margin-top: 20px;
    display: flex;
    justify-content: flex-end;
  }
}

.dialog-footer {
  padding-top: 20px;
  text-align: right;
}
</style> 