from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy import select

from app.database.base import Base
from app.database.connection import engine, get_db
from app.models.user import User
from app.schemas.user import UserCreate
from app.auth.password import hash_password

app = FastAPI()

Base.metadata.create_all(bind=engine)


@app.get("/")
def root():
    return {"message": "Hello World"}


@app.post("/signup")
def sign_up(user: UserCreate, db=Depends(get_db)):
    existing_user = db.scalar(
        select(User).where(User.email_id == user.email_id)
    )

    if existing_user:
        raise HTTPException(status_code=400, detail="User already exists")

    new_user = User(
        user_name=user.user_name,
        email_id=user.email_id,
        hashed_password=hash_password(user.password),
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {"message": "User created", "user_id": new_user.user_id, "email" : new_user.email_id}