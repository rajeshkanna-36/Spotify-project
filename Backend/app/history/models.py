from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import Integer, Text,BigInteger, ForeignKey, DATETIME, DateTime
from datetime import datetime,timezone
from app.database.base import Base
from app.songs.models import SongDetails
from app.users.models import User

class history(Base):

    __tablename__ = "history"

    history_id : Mapped[int] = mapped_column(
        BigInteger, primary_key=True, nullable=False
    )

    user_id : Mapped[int] = mapped_column(
        BigInteger, ForeignKey(User.user_id), nullable=False
    )

    song_id : Mapped[int]= mapped_column(
        BigInteger, ForeignKey(SongDetails.song_id), nullable=False
    )

    played_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        default=lambda: datetime.now(timezone.utc)
    )