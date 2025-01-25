<template>
  <div class="dashboard">
    <el-row :gutter="20">
      <el-col :span="6">
        <el-card class="stat-card">
          <template #header>
            <div class="card-header">
              <span>总用户数</span>
              <el-icon class="icon"><User /></el-icon>
            </div>
          </template>
          <div class="card-content">
            <span class="number">{{ stats.totalUsers }}</span>
            <span class="label">位用户</span>
          </div>
        </el-card>
      </el-col>
      <el-col :span="6">
        <el-card class="stat-card">
          <template #header>
            <div class="card-header">
              <span>今日新增</span>
              <el-icon class="icon"><UserFilled /></el-icon>
            </div>
          </template>
          <div class="card-content">
            <span class="number">{{ stats.newUsers }}</span>
            <span class="label">位用户</span>
          </div>
        </el-card>
      </el-col>
      <el-col :span="6">
        <el-card class="stat-card">
          <template #header>
            <div class="card-header">
              <span>活跃用户</span>
              <el-icon class="icon"><Star /></el-icon>
            </div>
          </template>
          <div class="card-content">
            <span class="number">{{ stats.activeUsers }}</span>
            <span class="label">位用户</span>
          </div>
        </el-card>
      </el-col>
      <el-col :span="6">
        <el-card class="stat-card">
          <template #header>
            <div class="card-header">
              <span>系统状态</span>
              <el-icon class="icon"><Monitor /></el-icon>
            </div>
          </template>
          <div class="card-content">
            <span class="status" :class="{ 'is-active': stats.systemStatus }">
              {{ stats.systemStatus ? '运行中' : '已停止' }}
            </span>
          </div>
        </el-card>
      </el-col>
    </el-row>

    <el-row :gutter="20" class="chart-row">
      <el-col :span="12">
        <el-card class="chart-card">
          <template #header>
            <div class="card-header">
              <span>用户增长趋势</span>
            </div>
          </template>
          <div class="chart-placeholder">
            图表区域（用户增长趋势）
          </div>
        </el-card>
      </el-col>
      <el-col :span="12">
        <el-card class="chart-card">
          <template #header>
            <div class="card-header">
              <span>活跃度分析</span>
            </div>
          </template>
          <div class="chart-placeholder">
            图表区域（活跃度分析）
          </div>
        </el-card>
      </el-col>
    </el-row>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import { User, UserFilled, Star, Monitor } from '@element-plus/icons-vue'

const stats = ref({
  totalUsers: 1234,
  newUsers: 56,
  activeUsers: 789,
  systemStatus: true
})
</script>

<style lang="scss" scoped>
.dashboard {
  .stat-card {
    margin-bottom: 20px;
    
    .card-header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      
      .icon {
        font-size: 20px;
        color: #409eff;
      }
    }
    
    .card-content {
      text-align: center;
      padding: 20px 0;
      
      .number {
        font-size: 36px;
        font-weight: bold;
        color: #303133;
        margin-right: 8px;
      }
      
      .label {
        color: #909399;
      }
      
      .status {
        font-size: 24px;
        font-weight: bold;
        color: #f56c6c;
        
        &.is-active {
          color: #67c23a;
        }
      }
    }
  }
  
  .chart-row {
    margin-top: 20px;
  }
  
  .chart-card {
    height: 400px;
    
    .chart-placeholder {
      height: 100%;
      display: flex;
      justify-content: center;
      align-items: center;
      color: #909399;
      font-size: 14px;
      background-color: #f5f7fa;
      border-radius: 4px;
    }
  }
}
</style> 