"""
用户相关API路由模块
包含用户注册、登录、信息管理等接口
"""

from typing import Any, List
from fastapi import APIRouter, Body, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app.crud import user as user_crud
from app.api import deps
from app.core.config import settings
from app.core import security
from app.schemas.user import User, UserCreate, UserUpdate, Token
from app.models.user import User as UserModel
from datetime import timedelta

router = APIRouter()

@router.get("/me", response_model=User)
def read_user_me(
    current_user: UserModel = Depends(deps.get_current_active_user),
) -> Any:
    """
    获取当前登录用户信息
    
    Args:
        current_user: 当前登录用户，通过token获取
        
    Returns:
        User: 用户信息
    """
    return current_user

@router.post("/register", response_model=User)
def register(
    *,
    db: Session = Depends(deps.get_db),
    user_in: UserCreate,
) -> Any:
    """
    注册新用户
    
    Args:
        db: 数据库会话
        user_in: 用户注册信息
        
    Returns:
        User: 创建的用户信息
        
    Raises:
        HTTPException: 邮箱已存在或用户名已存在时抛出
    """
    # 检查邮箱是否已存在
    user = user_crud.get_user_by_email(db, email=user_in.email)
    if user:
        raise HTTPException(
            status_code=400,
            detail="该邮箱已被注册",
        )
    # 检查用户名是否已存在
    user = user_crud.get_user_by_username(db, username=user_in.username)
    if user:
        raise HTTPException(
            status_code=400,
            detail="该用户名已被使用",
        )
    # 创建新用户
    user = user_crud.create_user(db, user=user_in)
    # 如果是第一个用户，设置为管理员
    if user.id == 1:
        user.is_admin = True
        db.commit()
    return user

@router.post("/login/access-token", response_model=Token)
def login_access_token(
    db: Session = Depends(deps.get_db),
    form_data: OAuth2PasswordRequestForm = Depends()
) -> Any:
    """
    用户登录获取访问令牌
    
    Args:
        db: 数据库会话
        form_data: 登录表单数据
        
    Returns:
        Token: 包含访问令牌的响应
        
    Raises:
        HTTPException: 用户名密码错误或用户被禁用时抛出
    """
    user = user_crud.authenticate_user(
        db, form_data.username, form_data.password
    )
    if not user:
        raise HTTPException(
            status_code=400, detail="用户名或密码错误"
        )
    elif not user.is_active:
        raise HTTPException(status_code=400, detail="用户已被禁用")
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    return {
        "access_token": security.create_access_token(
            user.id, expires_delta=access_token_expires
        ),
        "token_type": "bearer",
    }

@router.post("/users", response_model=User)
def create_user(
    *,
    db: Session = Depends(deps.get_db),
    user_in: UserCreate,
    current_user: UserModel = Depends(deps.get_current_active_admin)
) -> Any:
    """Create new user."""
    user = user_crud.get_user_by_email(db, email=user_in.email)
    if user:
        raise HTTPException(
            status_code=400,
            detail="该邮箱已被注册",
        )
    user = user_crud.get_user_by_username(db, username=user_in.username)
    if user:
        raise HTTPException(
            status_code=400,
            detail="该用户名已被使用",
        )
    user = user_crud.create_user(db, user=user_in)
    return user

@router.get("/users", response_model=List[User])
def read_users(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    current_user: UserModel = Depends(deps.get_current_active_admin)
) -> Any:
    """
    获取用户列表（仅管理员可用）
    
    Args:
        db: 数据库会话
        skip: 分页起始位置
        limit: 分页大小
        current_user: 当前登录用户（必须是管理员）
        
    Returns:
        List[User]: 用户列表
    """
    users = user_crud.get_users(db, skip=skip, limit=limit)
    return users

@router.get("/users/{user_id}", response_model=User)
def read_user(
    user_id: int,
    current_user: UserModel = Depends(deps.get_current_user),
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    获取指定用户信息
    
    Args:
        user_id: 用户ID
        current_user: 当前登录用户
        db: 数据库会话
        
    Returns:
        User: 用户信息
        
    Raises:
        HTTPException: 无权限访问时抛出
    """
    user = user_crud.get_user(db, user_id=user_id)
    if user == current_user or current_user.is_admin:
        return user
    raise HTTPException(
        status_code=400, detail="没有足够的权限"
    )

@router.put("/users/{user_id}", response_model=User)
def update_user(
    *,
    db: Session = Depends(deps.get_db),
    user_id: int,
    user_in: UserUpdate,
    current_user: UserModel = Depends(deps.get_current_active_admin)
) -> Any:
    """
    更新用户信息（仅管理员可用）
    
    Args:
        db: 数据库会话
        user_id: 用户ID
        user_in: 更新的用户信息
        current_user: 当前登录用户（必须是管理员）
        
    Returns:
        User: 更新后的用户信息
        
    Raises:
        HTTPException: 用户不存在时抛出
    """
    user = user_crud.get_user(db, user_id=user_id)
    if not user:
        raise HTTPException(
            status_code=404,
            detail="用户不存在",
        )
    user = user_crud.update_user(db, user_id=user_id, user=user_in)
    return user

@router.delete("/users/{user_id}", response_model=User)
def delete_user(
    *,
    db: Session = Depends(deps.get_db),
    user_id: int,
    current_user: UserModel = Depends(deps.get_current_active_admin)
) -> Any:
    """删除用户"""
    user = user_crud.get_user(db, user_id=user_id)
    if not user:
        raise HTTPException(
            status_code=404,
            detail="用户不存在",
        )
    user = user_crud.delete_user(db, user_id=user_id)
    return user 