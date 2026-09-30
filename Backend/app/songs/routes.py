from fastapi import APIRouter, Depends, HTTPException, UploadFile, File, Form
from sqlalchemy import select
from uuid import uuid4

from app.database.connection import get_db
from app.songs.models import SongDetails
from app.albums.models import album
from app.storage.s3 import upload_mp3
from app.auth.dependency import get_current_admin
from app.auth.checker import check_admin


router = APIRouter(
    prefix="/song",
    tags=["Songs"]
)


@router.post("/add_song")
def add_song(
    admin=Depends(get_current_admin),
    song_name: str = Form(...),
    album_id: int = Form(...),
    song_cover_key: str = Form(...),
    duration_ms: int = Form(...),
    file: UploadFile = File(...),
    db=Depends(get_db)
):

    check_admin(admin.admin_id, db)

    # Check MP3
    if file.content_type != "audio/mpeg":
        raise HTTPException(
            status_code=400,
            detail="Only MP3 files are allowed"
        )

    # Check album
    exist_album = db.scalar(
        select(album).where(
            album.album_id == album_id
        )
    )

    if not exist_album:
        raise HTTPException(
            status_code=404,
            detail="Album not found"
        )

    # Generate S3 object key
    object_key = f"songs/{uuid4()}.mp3"

    # Upload MP3 to S3
    upload_mp3(
        file.file,
        object_key
    )

    # Create database record
    new_song = SongDetails(
        song_name=song_name,
        album_id=album_id,
        song_key=object_key,
        song_cover_key=song_cover_key,
        duration_ms=duration_ms
    )

    db.add(new_song)
    db.commit()
    db.refresh(new_song)

    return new_song
