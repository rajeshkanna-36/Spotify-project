from fastapi import HTTPException
from sqlalchemy import select
from app.database.connection import get_db as db

# function to check the admin in db
def check_admin(admin : int):
    exists_admin = db.scalar(
        select(admin).where(
            admin.admin_id == admin.admin_id
        )
    )
    if not exists_admin:
        raise HTTPException(
            status_code=404,
            detail="Admin not found"
        )

# function to check the user in db
def check_user(user : int):
    exists_user = db.scalar(
        select(user).where(
            user.user_id == user.user_id
        )
    )
    if not exists_user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )