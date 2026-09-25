from sqlalchemy.orm import Mapped,mapped_column
from sqlalchemy import Text, Integer,String

from app.database.base import Base

class artist(Base):

    __tablename__ = "artist"

    artist_id : Mapped[int] = mapped_column(
        Integer,
        primary_key = True,
        index = True
    )

    artist_name : Mapped[str] = mapped_column(
        Text,
        nullable = False
    )