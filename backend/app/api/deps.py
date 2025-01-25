"""
API依赖模块
提供FastAPI依赖注入所需的函数，如数据库会话、当前用户等
"""

from typing import Generator, Optional
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from sqlalchemy.orm import Session
from app import crud
from app.core.config import settings
from app.db.session import SessionLocal
from app.models.user import User

# 配置OAuth2密码流认证
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login/access-token")

def get_db() -> Generator:
    """
    获取数据库会话的依赖函数
    
    Yields:
        Session: 数据库会话对象
        
    Note:
        使用yield语句使其可以在FastAPI依赖注入系统中使用
        在请求结束时自动关闭数据库会话
    """
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

def get_current_user(
    db: Session = Depends(get_db),
    token: str = Depends(oauth2_scheme)
) -> User:
    """
    获取当前用户的依赖函数
    
    Args:
        db: 数据库会话
        token: JWT令牌
        
    Returns:
        User: 当前用户对象
        
    Raises:
        HTTPException: 令牌无效或过期时抛出401错误
    """
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="登录已过期，请重新登录",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        # 解码JWT令牌
        payload = jwt.decode(
            token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM]
        )
        user_id: Optional[int] = payload.get("sub")
        if user_id is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    
    # 获取用户信息
    user = crud.user.get_user(db, user_id=int(user_id))
    if user is None:
        raise credentials_exception
    return user

def get_current_active_user(
    current_user: User = Depends(get_current_user),
) -> User:
    """
    获取当前活跃用户的依赖函数
    
    Args:
        current_user: 当前用户对象
        
    Returns:
        User: 当前活跃用户对象
        
    Raises:
        HTTPException: 用户未激活时抛出400错误
    """
    if not current_user.is_active:
        raise HTTPException(status_code=400, detail="用户未激活")
    return current_user

def get_current_active_admin(
    current_user: User = Depends(get_current_active_user),
) -> User:
    """
    获取当前管理员用户的依赖函数
    
    Args:
        current_user: 当前活跃用户对象
        
    Returns:
        User: 当前管理员用户对象
        
    Raises:
        HTTPException: 用户不是管理员时抛出403错误
    """
    if not current_user.is_admin:
        raise HTTPException(
            status_code=403, detail="权限不足"
        )
    return current_user 
    return current_user 