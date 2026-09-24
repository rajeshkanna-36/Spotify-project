from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from app.database.connection import get_db
from app.models.user import User
from app.models.session_table import SessionTable
from datetime import datetime, timezone

from app.schemas.user import UserCreate, UserLogin
from app.auth.password import hash_password, verify_password
from app.auth.jwt import create_access_token
from app.auth.dependency import get_current_user
from fastapi.security import HTTPBearer

auth_scheme = HTTPBearer()

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
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

    access_token,expire_at = create_access_token(existing_user.user_id)
    session = SessionTable(
        user_id = existing_user.user_id,
        token = access_token,
        created_at = datetime.now(timezone.utc),
        expire_at = expire_at,
        revoked = False
    )

    db.add(session)
    db.commit()
    db.refresh(session)

    return {
        "message" : "Login successful",
        "access_token" : access_token,
        "token_type": "bearer"
    }

@router.post("/logout")
def logout(token = Depends(auth_scheme),db=Depends(get_db)):
    
    session = db.scalar(
        select(SessionTable).where(
            SessionTable.token == token.credentials
        )
    )

    if not session:
        raise HTTPException(status_code=401, detail="Session does not exist")
    
    session.revoked = True
    session.expire_at = datetime.now(timezone.utc)
    db.commit()
    db.refresh(session)

    return {
        "message" : "Logout successful"
    }

@router.get("/me")
def check_user(user=Depends(get_current_user)):
    return user
    