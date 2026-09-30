from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session
from app.admin.model import Admin
from app.users.models import User


def check_admin(admin_id: int, db: Session):
    exists_admin = db.scalar(
        select(Admin).where(
            Admin.admin_id == admin_id
        )
    )
    if not exists_admin:
        raise HTTPException(
            status_code=404,
            detail="Admin not found"
        )
    return exists_admin

def check_user(user_id: int, db: Session):
    exists_user = db.scalar(
        select(User).where(
            User.user_id == user_id
        )
    )
    if not exists_user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )
    return exists_user