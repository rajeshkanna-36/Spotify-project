
from fastapi import FastAPI, Depends, HTTPException

from app.database.base import Base
from app.database.connection import engine, get_db
from app.models.user import User
from app.schemas.user import UserCreate, UserLogin
from sqlalchemy import select
from app.auth.password import hash_password, verify_password
from app.auth.jwt import create_access_token

app = FastAPI()

Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
    return {"message": "Hello World"}


@app.post("/signup")
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

@app.post("/login")
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
    
    