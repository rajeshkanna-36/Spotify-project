from fastapi import Depends , HTTPException
from fastapi.security import HTTPBearer
from jose import jwt 
from app.config.settings import JWT_SECRET_KEY, JWT_ALGORITHM
from app.database.connection import get_db
from app.models.user import User
from sqlalchemy import select

auth_scheme = HTTPBearer()

def get_current_user(token = Depends(auth_scheme), db = Depends(get_db)):
    payload = jwt.decode(
        token.credentials,
        JWT_SECRET_KEY,
        algorithms=[JWT_ALGORITHM]
    )

    user_id = payload["sub"]

    user = db.scalar(
        select(User).where(User.user_id == user_id)
    )

    if not user:
        raise HTTPException(
            status_code=401,
            detail="Invalid credentials"
        )

    return user

    