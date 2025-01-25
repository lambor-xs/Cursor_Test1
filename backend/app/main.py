"""
FastAPI主应用模块
负责创建和配置FastAPI应用实例，包括数据库初始化、中间件配置和路由注册
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.v1.endpoints import users
from app.core.config import settings
from app.db.session import engine
from app.models.user import Base

# 初始化数据库表
# 根据模型定义创建数据库表，如果表已存在则不会重复创建
Base.metadata.create_all(bind=engine)

# 创建FastAPI应用实例
app = FastAPI(
    title=settings.PROJECT_NAME,  # 设置应用名称
    openapi_url=f"{settings.API_V1_STR}/openapi.json"  # 设置OpenAPI文档URL
)

# 配置CORS（跨源资源共享）中间件
# 允许前端应用访问后端API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 允许所有来源访问
    allow_credentials=True,  # 允许携带认证信息（cookies等）
    allow_methods=["*"],  # 允许所有HTTP方法
    allow_headers=["*"],  # 允许所有请求头
)

# 注册路由模块
# 将用户相关的路由注册到应用
app.include_router(users.router, prefix="/api/v1", tags=["users"]) 