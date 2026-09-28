from fastapi import APIRouter,Depends,HTTPException

from app.models.user import user
from app.models.playlist import Playlist
from app.models.playlist_song import playlist_song
from app.schemas.PlaylistCreation import playlist_create,playlist_add
from app.database.connection import get_db
from sqlalchemy import select

router = APIRouter(
    prefix="/playlist",
    tags=["Playlists"]
)

@router.post("/create_playlist")
def create_playlist( playlist_data : playlist_create, db = Depends(get_db)):

    exist_playlist = db.scalar(
        select(Playlist).where(Playlist.playlist_id==playlist_data.playlist_id)
    )

    if exist_playlist :
        raise HTTPException(status_code=404,detail="Playlist already exists")
    
    new_playlist = Playlist(
        user_id = playlist_data.user_id,
        playlist_name = playlist_data.playlist_name,
        created_at = playlist_data.created_at
    )

    db.add(new_playlist)
    db.commit()
    db.refresh(new_playlist)

    return {
        "message": "Playlist created successfully",
        "playlist_id": new_playlist.playlist_id
    }

@router.put("/add_song")
def add_song( playlist_add_data: playlist_add, db = Depends(get_db)):
    
    exist_song = db.scalar(
        select(playlist_song).where(playlist_song.playlist_id==playlist_add_data.playlist_id)
    )
    
    if exist_song:
        raise HTTPException(status_code=404,detail="Song already exists in playlist")

    new_song = playlist_song(
        playlist_id = playlist_add_data.playlist_id,
        song_id = playlist_add_data.song_id,
        position = playlist_add_data.position
    )

    db.add(new_song)
    db.commit()
    db.refresh(new_song)

    return {
        "message": "Song added successfully",
        "playlist_id": new_song.playlist_id,
        "song_id": new_song.song_id
    }