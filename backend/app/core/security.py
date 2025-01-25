"""
安全相关工具模块
包含密码加密、JWT令牌生成等安全相关功能
"""

from datetime import datetime, timedelta
from typing import Any, Union
from jose import jwt
from passlib.context import CryptContext
from app.core.config import settings

# 创建密码加密上下文，使用bcrypt算法
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def create_access_token(
    subject: Union[str, Any], expires_delta: timedelta = None
) -> str:
    """
    创建访问令牌
    
    Args:
        subject: 令牌主题（通常是用户ID）
        expires_delta: 过期时间增量，如果不指定则使用默认配置
        
    Returns:
        str: 生成的JWT令牌
    """
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(
            minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
        )
    # 创建令牌数据
    to_encode = {"exp": expire, "sub": str(subject)}
    # 使用配置的密钥和算法进行加密
    encoded_jwt = jwt.encode(
        to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM
    )
    return encoded_jwt

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    验证密码
    
    Args:
        plain_password: 明文密码
        hashed_password: 加密后的密码
        
    Returns:
        bool: 密码是否匹配
    """
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password: str) -> str:
    """
    获取密码的哈希值
    
    Args:
        password: 明文密码
        
    Returns:
        str: 加密后的密码哈希值
    """
    return pwd_context.hash(password) 