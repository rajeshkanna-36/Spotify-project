from sqlalchemy import BigInteger, Text, Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from app.database.base import Base


class SongDetails(Base):
    __tablename__ = "song_details"

    song_id: Mapped[int] = mapped_column(
        BigInteger,
        primary_key=True,
        index=True
    )

    song_name: Mapped[str] = mapped_column(
        Text,
        nullable=False
    )

    album_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("album.album_id"),
        nullable=False
    )

    song_key: Mapped[str] = mapped_column(
        Text,
        nullable=False
    )

    song_cover_key: Mapped[str] = mapped_column(
        Text,
        nullable=False
    )

    duration_ms: Mapped[int] = mapped_column(
        Integer,
        nullable=False
    )