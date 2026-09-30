from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer
from jose import jwt

from app.core.settings import JWT_SECRET_KEY, JWT_ALGORITHM
from app.database.connection import get_db
from app.users.models import User
from app.admin.model import Admin
from app.auth.models import SessionTable
from sqlalchemy import select
from datetime import datetime, timezone
from app.admin.model import admin


auth_scheme = HTTPBearer()


def get_current_user(
    token=Depends(auth_scheme),
    db=Depends(get_db)
):
    payload = jwt.decode(
        token.credentials,
        JWT_SECRET_KEY,
        algorithms=[JWT_ALGORITHM]
    )

    if payload.get("type") != "user":
        raise HTTPException(
            status_code=401,
            detail="Invalid user token"
        )

    user_id = int(payload["sub"])

    session = db.scalar(
        select(SessionTable).where(
            SessionTable.user_id == user_id,
            SessionTable.token == token.credentials,
            SessionTable.expire_at > datetime.now(timezone.utc),
            SessionTable.revoked == False
        )
    )

    if not session:
        raise HTTPException(
            status_code=401,
            detail="Invalid credentials"
        )

    user = db.scalar(
        select(User).where(
            User.user_id == user_id
        )
    )

    if not user:
        raise HTTPException(
            status_code=401,
            detail="User not found"
        )

    return user


def get_current_admin(
    token=Depends(auth_scheme),
    db=Depends(get_db)
):
    payload = jwt.decode(
        token.credentials,
        JWT_SECRET_KEY,
        algorithms=[JWT_ALGORITHM]
    )

    if payload.get("type") != "admin":
        raise HTTPException(
            status_code=401,
            detail="Invalid admin token"
        )

    admin_id = int(payload["sub"])

    session = db.scalar(
        select(SessionTable).where(
            SessionTable.admin_id == admin_id,
            SessionTable.token == token.credentials,
            SessionTable.expire_at > datetime.now(timezone.utc),
            SessionTable.revoked == False
        )
    )

    if not session:
        raise HTTPException(
            status_code=401,
            detail="Invalid credentials"
        )

    admin_record = db.scalar(
        select(Admin).where(
            Admin.admin_id == admin_id
        )
    )

    if not admin_record:
        raise HTTPException(
            status_code=401,
            detail="Admin not found"
        )

    return admin_record
