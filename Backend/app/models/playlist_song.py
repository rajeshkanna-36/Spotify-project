from sqlalchemy.orm import Mapped,mapped_column
from sqlalchemy import BigInteger,Integer,ForeignKey
from app.database.base import Base

class playlist_song(Base):
    __tablename__ = "playlist_song"

    playlist_id:Mapped[int] = mapped_column(BigInteger,ForeignKey("playlist.playlist_id"),primery_key = True,nullable=False)
    song_id:Mapped[int] = mapped_column(BigInteger,ForeignKey("song_details.song_id"),primery_key = True,nullable=False)
    position:Mapped[int] = mapped_column(Integer,nullable=False)
