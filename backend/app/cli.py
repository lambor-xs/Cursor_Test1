"""
命令行工具模块
提供命令行接口用于系统管理，如创建管理员用户等
"""

import typer
from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app.crud.user import create_user
from app.schemas.user import UserCreate

# 创建命令行应用实例
app = typer.Typer()

def get_db() -> Session:
    """
    获取数据库会话
    
    Returns:
        Session: 数据库会话对象
        
    Note:
        使用完毕后会自动关闭会话
    """
    db = SessionLocal()
    try:
        return db
    finally:
        db.close()

@app.command()
def create_admin(
    username: str = typer.Option(..., prompt=True),  # 用户名，必填
    email: str = typer.Option(..., prompt=True),     # 邮箱，必填
    password: str = typer.Option(..., prompt=True, hide_input=True),  # 密码，必填且隐藏输入
):
    """
    创建管理员用户
    
    Args:
        username: 管理员用户名
        email: 管理员邮箱
        password: 管理员密码
        
    Note:
        所有参数都会通过命令行交互方式获取
        密码输入时不会显示字符
    """
    db = get_db()
    # 创建用户数据
    user = UserCreate(
        username=username,
        email=email,
        password=password,
        is_active=True
    )
    try:
        # 创建用户
        db_user = create_user(db, user)
        # 设置为管理员
        db_user.is_admin = True
        db.commit()
        typer.echo(f"管理员用户 {username} 创建成功！")
    except Exception as e:
        typer.echo(f"创建失败：{str(e)}")
        raise typer.Exit(1)

if __name__ == "__main__":
    app() 