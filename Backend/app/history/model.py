from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import Integer, Text,BigInteger, ForeignKey, DATETIME
from datetime import datetime
from app.database.base import Base
from app.songs.models import SongDetails

class history(Base):

    __tablename__ = "history"

    history_id : Mapped[int] = mapped_column(
        BigInteger, primary_key=True, nullable=False
    )

    song_id : Mapped[int]= mapped_column(
        BigInteger, ForeignKey(SongDetails.song_id), nullable=False
    )

    date : Mapped[datetime] = mapped_column(
        DATETIME, nullable=False
    )