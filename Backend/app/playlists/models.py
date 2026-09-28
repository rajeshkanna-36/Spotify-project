
from sqlalchemy.orm import Mapped,mapped_column
from sqlalchemy import Text, BigInteger,TIMESTAMP,ForeignKey,Integer
from app.database.base import Base
from datetime import datetime

class Playlist(Base):
    __tablename__ = "playlist"

    playlist_id:Mapped[int] = mapped_column(BigInteger,primary_key=True)
    user_id:Mapped[int] = mapped_column(BigInteger, ForeignKey("User.user_id"),nullable=False)
    playlist_name:Mapped[str] = mapped_column(Text,nullable=False)
    created_at:Mapped[datetime] = mapped_column(TIMESTAMP,nullable=False)


class playlist_song(Base):
    __tablename__ = "playlist_song"

    playlist_id:Mapped[int] = mapped_column(BigInteger,ForeignKey("playlist.playlist_id"),primary_key=True,nullable=False)
    song_id:Mapped[int] = mapped_column(BigInteger,ForeignKey("song_details.song_id"),primary_key=True,nullable=False)
    position:Mapped[int] = mapped_column(Integer,nullable=False)
