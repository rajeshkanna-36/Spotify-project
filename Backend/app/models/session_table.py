from sqlalchemy import BigInteger,Text,DateTime,Boolean
from sqlalchemy.orm import mapped_column, Mapped
from app.database.base import Base
from datetime import datetime

class SessionTable(Base):
    __tablename__ = "SessionTable"

    session_id: Mapped[int] = mapped_column(
        BigInteger,
        primary_key=True,
        index=True
    )

    user_id : Mapped[int] = mapped_column(
        BigInteger,
        nullable=False
    )

    token : Mapped[str]=mapped_column(
        Text,
        unique=True,
        nullable=False
    )

    created_at : Mapped[datetime]= mapped_column(
        DateTime,
        nullable=False
    )

    expire_at : Mapped[datetime]=mapped_column(
        DateTime,
        nullable=False
    )

    revoked : Mapped[bool] = mapped_column(
        Boolean,
        nullable=False,
        default=False
    )

    

    
