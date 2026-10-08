from fastapi import APIRouter, Depends, HTTPException, UploadFile, File, Form
from sqlalchemy import select
from uuid import uuid4

from app.database.connection import get_db
from app.songs.models import SongDetails
from app.albums.models import album
from app.storage.s3 import upload_mp3,upload_cover_image
from app.auth.dependency import get_current_admin
from app.auth.checker import check_admin
from app.storage.s3 import delete_objects
from app.songs.models import song_artist
from app.playlists.models import playlist_song


router = APIRouter(
    prefix="/song",
    tags=["Songs"]
)


@router.post("/add_song")
def add_song(
    admin=Depends(get_current_admin),
    song_name: str = Form(...),
    album_id: int = Form(...),
    duration_ms: int = Form(...),
    cover_image: UploadFile = File(...),
    song_file: UploadFile = File(...),
    db=Depends(get_db)
):
    check_admin(admin.admin_id, db)

    # Check MP3
    if song_file.content_type != "audio/mpeg":
        raise HTTPException(
            status_code=400,
            detail="Only MP3 files are allowed"
        )

    # Check image
    allowed_images = {
        "image/jpeg",
        "image/png",
        "image/webp"
    }

    if cover_image.content_type not in allowed_images:
        raise HTTPException(
            status_code=400,
            detail="Only JPG, PNG and WEBP images are allowed"
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

    # Generate S3 keys
    song_key = f"songs/{uuid4()}.mp3"
    cover_key = f"covers/{uuid4()}"

    # Upload MP3
    upload_mp3(
        song_file.file,
        song_key
    )

    # Upload cover
    upload_cover_image(
        cover_image.file,
        cover_key,
        cover_image.content_type
    )

    # Create DB record
    new_song = SongDetails(
        song_name=song_name,
        album_id=album_id,
        song_key=song_key,
        song_cover_key=cover_key,
        duration_ms=duration_ms
    )

    db.add(new_song)
    db.commit()
    db.refresh(new_song)

    return {
        new_song.song_id:"Sucessfully uploaded"}

@router.delete("/delete_song/{song_id}")
def delete_song(song_id:int,admin=Depends(get_current_admin), db=Depends(get_db)):
    check_admin(admin.admin_id, db)
    
    exists_song = db.scalar(
        select(SongDetails).where(
            SongDetails.song_id == song_id
        )
    )
    if not exists_song:
        raise HTTPException(
            status_code=404,
            detail="Song not found"
        )

    delete_objects(exists_song.song_key)
    delete_objects(exists_song.song_cover_key)
    
    db.query(song_artist).filter(
        song_artist.song_id == song_id
    ).delete()

    db.query(playlist_song).filter(
        playlist_song.song_id == song_id
    ).delete()
    
    db.delete(exists_song)
    db.commit()
    
    return {
        "message": "Song deleted successfully"
    }