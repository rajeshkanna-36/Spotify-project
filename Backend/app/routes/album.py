from fastapi import Depends, HTTPException, APIRouter

from app.database.connection import get_db
from app.models.album import album
from app.schemas.AlbumCreation import add_album
from sqlalchemy import select

router = APIRouter(
    prefix="/album",
    tags=["Album"]
)

@router.post("/add_album")
def add_album(album : add_album, db = Depends(get_db)):

    existing_album = db.scalar(
        select(album).where(album.album_name == album.album_name)
    )

    if existing_album:
        raise HTTPException(status_code=400, detail="Album already exists")

    new_album = album(
        album_name = album.album_name,
        album_cover_key = album.album_cover_key
    )

    db.add(new_album)
    db.commit()
    db.refresh(new_album)