"""
系统配置模块
用于管理整个应用的配置信息，包括项目名称、API版本、安全设置等
"""

from pydantic_settings import BaseSettings
from typing import Optional
import os
from dotenv import load_dotenv

# 加载环境变量
load_dotenv()

class Settings(BaseSettings):
    """
    应用配置类
    包含所有系统级别的配置项
    """
    # 项目基本信息
    PROJECT_NAME: str = "Auto Card System"  # 项目名称
    API_V1_STR: str = "/api/v1"  # API版本路径

    # 安全相关配置
    SECRET_KEY: str = os.getenv("SECRET_KEY")  # JWT加密密钥
    ALGORITHM: str = os.getenv("ALGORITHM", "HS256")  # JWT加密算法
    ACCESS_TOKEN_EXPIRE_MINUTES: int = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "30"))  # 访问令牌过期时间

    # 数据库配置
    DATABASE_URL: str = os.getenv("DATABASE_URL")  # 数据库连接URL

    class Config:
        case_sensitive = True  # 配置键名大小写敏感

# 创建全局配置对象
settings = Settings() 