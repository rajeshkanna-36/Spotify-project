from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import select

from app.database.connection import get_db
from app.models.song import SongDetails
from app.models.album import album
from app.schemas.SongCreation import SongCreate


router = APIRouter(
    prefix="/song",
    tags=["Songs"]
)

@router.post("/add_song")
def add_song(song: SongCreate, db=Depends(get_db)):
    exist_album = db.scalar(
        select(album).where(album.album_id == song.album_id)
    )

    if not exist_album:
        raise HTTPException(
            status_code=404,
            detail="Album not found"
        )

    new_song = SongDetails(
        song_name=song.song_name,
        album_id=song.album_id,
        song_key=song.song_key,
        song_cover_key=song.song_cover_key,
        duration_ms=song.duration_ms
    )

    db.add(new_song)
    db.commit()
    db.refresh(new_song)

    return new_song