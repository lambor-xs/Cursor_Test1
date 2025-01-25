"""
用户数据模型模块
定义用户在数据库中的表结构和字段
"""

from sqlalchemy import Boolean, Column, Integer, String, DateTime
from sqlalchemy.sql import func
from app.db.base_class import Base

class User(Base):
    """
    用户数据模型
    
    Attributes:
        id: 用户ID，主键
        email: 用户邮箱，唯一
        username: 用户名，唯一
        hashed_password: 加密后的密码
        is_active: 是否激活
        is_admin: 是否为管理员
        created_at: 创建时间
        updated_at: 更新时间
    """
    __tablename__ = "users"  # 数据库表名

    # 用户基本信息
    id = Column(Integer, primary_key=True, index=True)  # 用户ID，主键
    email = Column(String(100), unique=True, index=True)  # 邮箱，唯一索引
    username = Column(String(100), unique=True, index=True)  # 用户名，唯一索引
    hashed_password = Column(String(255))  # 加密后的密码

    # 用户状态
    is_active = Column(Boolean, default=True)  # 是否激活
    is_admin = Column(Boolean, default=False)  # 是否为管理员

    # 时间戳
    created_at = Column(DateTime(timezone=True), server_default=func.now())  # 创建时间
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())  # 更新时间 