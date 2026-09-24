from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer
from jose import jwt

from app.config.settings import JWT_SECRET_KEY, JWT_ALGORITHM
from app.database.connection import get_db
from app.models.user import User
from app.models.session_table import SessionTable
from sqlalchemy import select
from datetime import datetime, timezone


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