from app.songs.models import SongDetails
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select

from app.database.connection import get_db
from app.albums.models import album as Album
from app.albums.schemas import add_album
from app.auth.checker import check_admin
from app.auth.dependency import get_current_admin
from app.storage.s3 import delete_objects
from app.artists.models import song_artist

router = APIRouter(
    prefix="/album",
    tags=["Album"]
)


@router.post("/add_album")
def add_album(album_data: add_album,admin=Depends(get_current_admin), db=Depends(get_db)):

    check_admin(admin.admin_id, db)
        
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

@router.delete("/album_delete/{album_id}")
def delete_album(album_id: int,admin=Depends(get_current_admin), db=Depends(get_db)):
    check_admin(admin.admin_id, db)
    
    exists_album = db.scalar(
        select(Album).where(
            Album.album_id == album_id
        )
    )
    if not exists_album:
        raise HTTPException(
            status_code=404,
            detail="Album not found"
        )
    
    songs = db.scalars(
        select(SongDetails).where(SongDetails.album_id==album_id)
    ).all()

    for song in songs:

        delete_objects(song.song_key)
        delete_objects(song.song_cover_key)
        
        db.query(song_artist).filter(
            song_artist.song_id == song.song_id
        ).delete()
        
        db.delete(song)

    delete_objects(exists_album.album_cover_key)
    
    db.delete(exists_album)
    db.commit()
    
    return {
        "message": "Album deleted"
    }


    