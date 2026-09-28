
from sqlalchemy.orm import Mapped,mapped_column
from sqlalchemy import Text, BigInteger,TIMESTAMP,ForeignKey
from app.database.base import Base
from datetime import datetime
from app.models.user import user

class Playlist(Base):
    __tablename__ = "playlist"

    playlist_id:Mapped[int] = mapped_column(BigInteger,primary_key=True)
    user_id:Mapped[int] = mapped_column(BigInteger, ForeignKey("User.user_id"),nullable=False)
    playlist_name:Mapped[str] = mapped_column(Text,nullable=False)
    created_at:Mapped[datetime] = mapped_column(TIMESTAMP,nullable=False)
    
    