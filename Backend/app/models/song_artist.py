from sqlalchemy import Integer, ForeignKey
from sqlalchemy.orm import Mapped,mapped_column
from app.database.base import Base

class song_artist(Base):
    __tablename__ = "song_artist"

    song_id : Mapped[int] = mapped_column(
        Integer,
        ForeignKey("song_details.song_id"),
        primary_key = True,
        index = True
    )

    artist_id : Mapped[int] = mapped_column(
        Integer,
        ForeignKey("artist.artist_id"),
        primary_key = True,
        index = True
    )

    
