"""
用户数据模式模块
定义用户相关的Pydantic模型，用于数据验证和序列化
"""

from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

class UserBase(BaseModel):
    """
    用户基础模型
    包含用户的基本信息字段
    """
    email: EmailStr  # 电子邮箱
    username: str    # 用户名
    is_active: Optional[bool] = True  # 是否激活

class UserCreate(UserBase):
    """
    用户创建模型
    继承自UserBase，添加密码字段
    """
    password: str  # 密码

class UserUpdate(BaseModel):
    """
    用户更新模型
    所有字段都是可选的，允许部分更新
    """
    email: Optional[EmailStr] = None  # 电子邮箱
    username: Optional[str] = None    # 用户名
    password: Optional[str] = None    # 密码
    is_active: Optional[bool] = None  # 是否激活

class UserInDBBase(UserBase):
    """
    数据库用户基础模型
    包含从数据库读取的用户完整信息
    """
    id: int  # 用户ID
    is_admin: bool  # 是否为管理员
    created_at: datetime  # 创建时间
    updated_at: Optional[datetime]  # 更新时间

    class Config:
        from_attributes = True  # 允许从ORM模型创建

class User(UserInDBBase):
    """
    用户响应模型
    用于向客户端返回用户信息
    """
    pass

class UserInDB(UserInDBBase):
    """
    数据库中的用户模型
    包含密码哈希等敏感信息
    """
    hashed_password: str  # 加密后的密码

class Token(BaseModel):
    """
    令牌模型
    用于用户认证
    """
    access_token: str  # 访问令牌
    token_type: str    # 令牌类型

class TokenPayload(BaseModel):
    """
    令牌载荷模型
    用于JWT令牌的内容
    """
    sub: Optional[int] = None  # 主题（通常是用户ID） 