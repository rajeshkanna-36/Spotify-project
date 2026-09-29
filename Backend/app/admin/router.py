from fastapi import Depends,FastAPI,HTTPException,status
from sqlalchemy.orm import Session
from app.database.connection import get_db
from app.admin.model import admin
from app.admin.schema import admin_signup
from sqlalchemy import select
from app.auth.password import hash_password,verify_password
from app.auth.jwt import create_access_token
from app.auth.models import SessionTable
from datetime import datetime, timezone

router = FastAPI()

@router.post("/signup")
async def admin_signup(admin_data:admin_signup,db:Session = Depends(get_db)):
    
    admin = db.scalar(
        select(admin).where(
            admin.admin_id == admin_data.admin_id
        )
    )

    if admin :
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Admin already exists"
        )
    
    admin = admin(
        admin_id = admin_data.admin_id,
        role = admin_data.role,
        password = hash_password(admin_data.password)
    )

    db.add(admin)
    db.commit()
    db.refresh(admin)
    return {
        "message" : "Admin created",
        "admin_id" : admin.admin_id
    }

@router.post("/login")
async def admin_login(admin_data:admin_login,db:Session = Depends(get_db)):
    
    admin = db.scalar(
        select(admin).where(
            admin.admin_id == admin_data.admin_id
        )
    )

    if not admin:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid admin_id or password"
        )

    if not verify_password(
        admin_data.password,
        admin.password
    ):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid admin_id or password"
        )
    access_token,expire_at = create_access_token(admin.admin_id)
    session = SessionTable(
        user_id = admin.admin_id,
        token = access_token,
        created_at = datetime.now(timezone.utc),
        expire_at = expire_at,
        revoked = False
    )
    return {
        "message" : "Admin login successful",
        "admin_id" : admin.admin_id,
        "access_token" : access_token,
        "token_type" : "bearer"
    }

    