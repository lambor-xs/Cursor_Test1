"""
数据库会话管理模块
负责创建和管理数据库连接池、会话等
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import QueuePool
import os
from dotenv import load_dotenv

# 加载环境变量
load_dotenv()

# 从环境变量获取数据库连接URL
SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL")

# 创建数据库引擎
# poolclass=QueuePool: 使用连接池
# pool_size=5: 连接池大小
# max_overflow=10: 允许的最大连接数超出pool_size的数量
# pool_timeout=30: 连接池获取连接的超时时间
# pool_recycle=1800: 连接在连接池中的回收时间(30分钟)
engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    poolclass=QueuePool,
    pool_size=5,
    max_overflow=10,
    pool_timeout=30,
    pool_recycle=1800
)

# 创建会话工厂
# autocommit=False: 不自动提交事务
# autoflush=False: 不自动刷新
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    """
    获取数据库会话的依赖函数
    
    Yields:
        Session: 数据库会话对象
        
    Note:
        使用yield语句使其可以在FastAPI依赖注入系统中使用
        在请求结束时自动关闭数据库会话
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close() 