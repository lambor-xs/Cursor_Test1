# 自动发卡系统

一个基于 FastAPI 和 Vue 3 开发的现代化自动发卡系统，提供用户管理、卡密管理、订单管理等功能。

## 技术栈

### 后端
- FastAPI：高性能的 Python Web 框架
- SQLAlchemy：ORM 框架
- Pydantic：数据验证
- JWT：身份认证
- Alembic：数据库迁移
- MySQL/SQLite：数据库

### 前端
- Vue 3：渐进式 JavaScript 框架
- TypeScript：类型安全的 JavaScript 超集
- Vite：现代前端构建工具
- Element Plus：Vue 3 组件库
- Pinia：状态管理
- Vue Router：路由管理
- Axios：HTTP 客户端

## 功能特性

- [x] 用户认证
  - 登录/注册
  - JWT 认证
  - 权限控制
- [x] 用户管理
  - 用户列表
  - 添加/编辑/删除用户
  - 用户状态管理
- [ ] 卡密管理
  - 卡密生成
  - 卡密导入/导出
  - 卡密状态管理
- [ ] 订单管理
  - 订单创建
  - 订单状态追踪
  - 订单统计
- [ ] 商品管理
  - 商品分类
  - 商品上下架
  - 价格管理
- [ ] 统计分析
  - 销售统计
  - 用户分析
  - 数据报表

## 快速开始

### 环境要求

- Python 3.9+
- Node.js 16+
- MySQL 5.7+ 或 SQLite 3

### 后端安装

1. 进入后端目录：
```bash
cd backend
```

2. 创建虚拟环境：
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\\Scripts\\activate  # Windows
```

3. 安装依赖：
```bash
pip install -r requirements.txt
```

4. 配置环境变量：
```bash
cp .env.example .env
# 编辑 .env 文件，配置数据库等信息
```

5. 创建数据库表：
```bash
alembic upgrade head
```

6. 创建管理员用户：
```bash
python -m app.cli create-admin
```

7. 启动服务：
```bash
uvicorn app.main:app --reload
```

### 前端安装

1. 进入前端目录：
```bash
cd frontend/admin
```

2. 安装依赖：
```bash
npm install
```

3. 配置环境变量：
```bash
cp .env.example .env
# 编辑 .env 文件，配置API地址等信息
```

4. 启动开发服务器：
```bash
npm run dev
```

5. 构建生产版本：
```bash
npm run build
```

## 项目结构

```
├── backend/                # 后端项目
│   ├── alembic/           # 数据库迁移
│   ├── app/               # 应用代码
│   │   ├── api/          # API路由
│   │   ├── core/         # 核心功能
│   │   ├── crud/         # 数据库操作
│   │   ├── models/       # 数据模型
│   │   └── schemas/      # 数据验证
│   └── requirements.txt   # 依赖清单
│
└── frontend/              # 前端项目
    └── admin/            # 管理后台
        ├── src/          # 源代码
        ├── public/       # 静态资源
        └── package.json  # 项目配置
```

## API 文档

启动后端服务后，访问以下地址查看 API 文档：
- Swagger UI：http://localhost:8000/docs
- ReDoc：http://localhost:8000/redoc

## 开发指南

### 代码规范
- 后端遵循 PEP 8 规范
- 前端遵循 Vue 3 风格指南
- 使用 ESLint 和 Prettier 保持代码风格统一

### 提交规范
提交信息格式：
```
<type>(<scope>): <subject>

<body>

<footer>
```

type 类型：
- feat: 新功能
- fix: 修复
- docs: 文档
- style: 格式
- refactor: 重构
- test: 测试
- chore: 构建

## 部署

### 后端部署
1. 使用 Gunicorn 作为 WSGI 服务器
2. 配置 Nginx 反向代理
3. 使用 Supervisor 管理进程

### 前端部署
1. 构建生产版本
2. 配置 Nginx 托管静态文件
3. 配置 HTTPS 证书

## 贡献指南

1. Fork 本仓库
2. 创建特性分支
3. 提交代码
4. 创建 Pull Request

## 许可证

本项目采用 MIT 许可证，详见 [LICENSE](LICENSE) 文件。

## 联系方式

如有问题或建议，请提交 Issue 或 Pull Request。 