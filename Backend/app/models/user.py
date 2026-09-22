from sqlalchemy import BigInteger, Text
from sqlalchemy.orm import Mapped, mapped_column

from app.database.base import Base


class User(Base):
    __tablename__ = "User"

    user_id: Mapped[int] = mapped_column(
        BigInteger,
        primary_key=True,
        index=True
    )

    user_name: Mapped[str] = mapped_column(
        Text,
        unique=True,
        nullable=False
    )

    email_id: Mapped[str] = mapped_column(
        Text,
        unique=True,
        nullable=False
    )

    hashed_password: Mapped[str] = mapped_column(
        Text,
        nullable=False
    )