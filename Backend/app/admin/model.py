from sqlalchemy import Integer, Text
from sqlalchemy.orm import Mapped, mapped_column

from app.database.base import Base

class admin (Base):

    admin_id : Mapped[int] = mapped_column(
        Integer, primary_key = True,nullable = False
    )

    role : Mapped[str] = mapped_column(
        Text, nullable = False
    )

    hashed_password : Mapped[str]=mapped_column(
        Text, nullable = False
    )