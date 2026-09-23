from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from app.database.connection import get_db
from app.models.user import User

from app.schemas.user import UserCreate, UserLogin
from app.auth.password import hash_password, verify_password
from app.auth.jwt import create_access_token
from app.auth.dependency import get_current_user

router = APIRouter(
    prefix="/auth",
    tags="Authentication"
)

@router.post("/signup")
def sign_up(
    user: UserCreate,
    db = Depends(get_db)
):
    existing_user = db.scalar(
        select(User).where(User.email_id == user.email_id)
    )

    if existing_user:
        raise HTTPException(status_code=400, detail="User already exists")

    user = User(
        user_name = user.user_name,
        email_id = user.email_id,
        hashed_password = hash_password(user.password)
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    return {
    "message": "User created",
    "user_id": user.user_id
    }

@router.post("/login")
def login(user: UserLogin,db=Depends(get_db)):
    existing_user = db.scalar(
        select(User).where(
            User.email_id == user.email_id
        )
    )

    if not existing_user:
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password"
        )

    if not verify_password(
        user.password,
        existing_user.hashed_password
    ):
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password"
        )

    access_token = create_access_token(existing_user.user_id)

    return {
        "message" : "Login successful",
        "access_token" : access_token,
        "token_type": "bearer"
    }
