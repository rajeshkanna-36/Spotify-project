from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select

from app.database.connection import get_db
from app.albums.models import album as Album
from app.albums.schemas import add_album
from app.auth.checker import check_admin
from app.auth.dependency import get_current_admin

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

@router.delete("/{album_id}")
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
    
    db.delete(exists_album)
    db.commit()
    
    return {
        "message": "Album deleted"
    }
    