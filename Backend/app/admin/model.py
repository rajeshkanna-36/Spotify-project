from sqlalchemy import Integer, Text, Enum
from sqlalchemy.orm import Mapped, mapped_column

from app.database.base import Base
from app.admin.schema import AdminRole


class Admin(Base):

    __tablename__ = "admin"

    admin_id: Mapped[int] = mapped_column(
        Integer, primary_key=True, nullable=False
    )

    role: Mapped[AdminRole] = mapped_column(
        Enum(AdminRole), nullable=False
    )

    hashed_password: Mapped[str] = mapped_column(
        Text, nullable=False
    )
