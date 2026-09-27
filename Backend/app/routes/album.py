from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select

from app.database.connection import get_db
from app.models.album import album as Album
from app.schemas.AlbumCreation import add_album


router = APIRouter(
    prefix="/album",
    tags=["Album"]
)


@router.post("/add_album")
def add_album(album_data: add_album, db=Depends(get_db)):

    existing_album = db.scalar(
        select(Album).where(
            Album.album_name == album_data.album_name
        )
    )

    if existing_album:
        raise HTTPException(
            status_code=400,
            detail="Album already exists"
        )

    new_album = Album(
        album_name=album_data.album_name,
        album_cover_key=album_data.album_cover_key
    )

    db.add(new_album)
    db.commit()
    db.refresh(new_album)

    return new_album