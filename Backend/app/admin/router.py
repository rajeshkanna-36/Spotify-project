from fastapi import Depends, APIRouter, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy import select
from datetime import datetime, timezone

from app.database.connection import get_db
from app.admin.model import Admin
from app.admin.schema import admin_signup, admin_login
from app.auth.password import hash_password, verify_password
from app.auth.jwt import create_admin_access_token
from app.auth.models import SessionTable


router = APIRouter(
    prefix="/admin",
    tags=["Admin"]
)


@router.post("/signup")
async def admin_signup_route(
    admin_data: admin_signup,
    db: Session = Depends(get_db)
):
    admin_record = db.scalar(
        select(Admin).where(
            Admin.admin_id == admin_data.admin_id
        )
    )

    if admin_record:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Admin already exists"
        )

    admin_record = Admin(
        admin_id=admin_data.admin_id,
        role=admin_data.role,
        hashed_password=hash_password(admin_data.password)
    )

    db.add(admin_record)
    db.commit()
    db.refresh(admin_record)

    return {
        "message": "Admin created",
        "admin_id": admin_record.admin_id
    }


@router.post("/login")
async def admin_login_route(
    admin_data: admin_login,
    db: Session = Depends(get_db)
):
    admin_record = db.scalar(
        select(Admin).where(
            Admin.admin_id == admin_data.admin_id
        )
    )

    if not admin_record:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid admin_id or password"
        )

    if not verify_password(
        admin_data.password,
        admin_record.hashed_password
    ):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid admin_id or password"
        )

    access_token, expire_at = create_admin_access_token(
        admin_record.admin_id,
        admin_record.role.value
    )

    session = SessionTable(
        admin_id=admin_record.admin_id,
        token=access_token,
        created_at=datetime.now(timezone.utc),
        expire_at=expire_at,
        revoked=False
    )

    db.add(session)
    db.commit()
    db.refresh(session)

    return {
        "message": "Admin login successful",
        "admin_id": admin_record.admin_id,
        "access_token": access_token,
        "token_type": "bearer"
    }
