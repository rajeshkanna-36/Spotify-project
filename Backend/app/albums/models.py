from sqlalchemy import Integer,Text
from sqlalchemy.orm import mapped_column,Mapped
from app.database.base import Base

class album(Base):

    __tablename__ = "album"

    album_id : Mapped[int]= mapped_column(
        Integer,
        primary_key = True,
        index = True 
    )

    album_name : Mapped[str]=mapped_column(
        Text,
        nullable = False
    )

    album_cover_key :Mapped[str]=mapped_column(
        Text,
        nullable = True
    )
