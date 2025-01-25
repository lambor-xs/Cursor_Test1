# 自动发卡系统项目结构

## 后端结构 (backend/)

```
backend/
├── alembic/                # 数据库迁移相关文件
├── app/                    # 主应用目录
│   ├── api/               # API相关代码
│   │   └── v1/           # API版本1
│   │       └── endpoints/ # API端点
│   │   ├── core/             # 核心功能
│   │   │   ├── config.py     # 配置管理
│   │   │   └── security.py   # 安全相关
│   │   ├── crud/             # 数据库操作
│   │   ├── db/               # 数据库配置
│   │   ├── models/           # 数据库模型
│   │   └── schemas/          # Pydantic模型
│   ├── logs/                  # 日志文件
│   ├── tests/                 # 测试文件
│   ├── .env                   # 环境变量
│   ├── alembic.ini           # Alembic配置
│   └── requirements.txt       # 项目依赖
```

## 前端结构 (frontend/admin/)

```
frontend/admin/
├── public/               # 静态资源
├── src/                  # 源代码
│   ├── api/             # API请求
│   ├── assets/          # 资源文件
│   │   ├── images/      # 图片
│   │   └── styles/      # 样式
│   ├── components/      # 公共组件
│   ├── layouts/         # 布局组件
│   ├── router/          # 路由配置
│   ├── stores/          # 状态管理
│   ├── types/           # TypeScript类型
│   ├── utils/           # 工具函数
│   └── views/           # 页面组件
│   ├── .env                 # 环境变量
│   ├── .env.development     # 开发环境变量
│   ├── .env.production      # 生产环境变量
│   ├── index.html           # HTML模板
│   ├── package.json         # 项目配置
│   ├── tsconfig.json        # TypeScript配置
│   └── vite.config.ts       # Vite配置
```

## 主要功能模块

### 后端模块
- 用户认证与授权
- 用户管理
- 卡密管理
- 订单管理
- 商品管理
- 统计分析

### 前端模块
- 登录/注册
- 用户管理
- 卡密管理
- 订单管理
- 商品管理
- 数据统计
- 系统设置

## 技术栈

### 后端
- FastAPI: Web框架
- SQLAlchemy: ORM
- Pydantic: 数据验证
- JWT: 身份认证
- Alembic: 数据库迁移
- MySQL/SQLite: 数据库

### 前端
- Vue 3: 前端框架
- TypeScript: 编程语言
- Vite: 构建工具
- Pinia: 状态管理
- Vue Router: 路由管理
- Element Plus: UI组件库
- Axios: HTTP客户端 