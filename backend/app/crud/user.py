"""
用户数据库操作模块
包含用户的增删改查等数据库操作函数
"""

from typing import Optional, List
from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.user import UserCreate, UserUpdate
from app.core.security import get_password_hash, verify_password

def get_user(db: Session, user_id: int) -> Optional[User]:
    """
    通过用户ID获取用户
    
    Args:
        db: 数据库会话
        user_id: 用户ID
        
    Returns:
        Optional[User]: 用户对象，如果不存在则返回None
    """
    return db.query(User).filter(User.id == user_id).first()

def get_user_by_email(db: Session, email: str) -> Optional[User]:
    """
    通过邮箱获取用户
    
    Args:
        db: 数据库会话
        email: 用户邮箱
        
    Returns:
        Optional[User]: 用户对象，如果不存在则返回None
    """
    return db.query(User).filter(User.email == email).first()

def get_user_by_username(db: Session, username: str) -> Optional[User]:
    """
    通过用户名获取用户
    
    Args:
        db: 数据库会话
        username: 用户名
        
    Returns:
        Optional[User]: 用户对象，如果不存在则返回None
    """
    return db.query(User).filter(User.username == username).first()

def get_users(
    db: Session, skip: int = 0, limit: int = 100
) -> List[User]:
    """
    获取用户列表
    
    Args:
        db: 数据库会话
        skip: 分页起始位置
        limit: 分页大小
        
    Returns:
        List[User]: 用户列表
    """
    return db.query(User).offset(skip).limit(limit).all()

def create_user(db: Session, user: UserCreate) -> User:
    """
    创建新用户
    
    Args:
        db: 数据库会话
        user: 用户创建模型
        
    Returns:
        User: 创建的用户对象
    """
    # 对密码进行哈希处理
    hashed_password = get_password_hash(user.password)
    # 创建用户对象
    db_user = User(
        email=user.email,
        username=user.username,
        hashed_password=hashed_password,
        is_active=user.is_active
    )
    # 保存到数据库
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def update_user(
    db: Session, user_id: int, user: UserUpdate
) -> Optional[User]:
    """
    更新用户信息
    
    Args:
        db: 数据库会话
        user_id: 用户ID
        user: 用户更新模型
        
    Returns:
        Optional[User]: 更新后的用户对象，如果用户不存在则返回None
    """
    db_user = get_user(db, user_id)
    if not db_user:
        return None
    
    # 获取更新数据
    update_data = user.model_dump(exclude_unset=True)
    # 如果更新密码，需要进行哈希处理
    if "password" in update_data:
        update_data["hashed_password"] = get_password_hash(update_data.pop("password"))
    
    # 更新用户属性
    for field, value in update_data.items():
        setattr(db_user, field, value)
    
    # 保存到数据库
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def delete_user(db: Session, user_id: int) -> Optional[User]:
    """
    删除用户
    
    Args:
        db: 数据库会话
        user_id: 用户ID
        
    Returns:
        Optional[User]: 被删除的用户对象，如果用户不存在则返回None
    """
    user = db.query(User).filter(User.id == user_id).first()
    if user:
        db.delete(user)
        db.commit()
    return user

def authenticate_user(
    db: Session, username: str, password: str
) -> Optional[User]:
    """
    验证用户身份
    
    Args:
        db: 数据库会话
        username: 用户名
        password: 密码
        
    Returns:
        Optional[User]: 验证成功返回用户对象，失败返回None
    """
    user = get_user_by_username(db, username)
    if not user:
        return None
    if not verify_password(password, user.hashed_password):
        return None
    return user 