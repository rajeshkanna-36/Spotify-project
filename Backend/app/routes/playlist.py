from fastapi import APIRouter,Depends,HTTPException

from app.models.playlist import Playlist
from app.models.playlist_song import playlist_song
from app.schemas.PlaylistCreation import playlist_create,playlist_add
from app.database.connection import get_db
from app.auth.dependency import get_current_user
from sqlalchemy import select

router = APIRouter(
    prefix="/playlist",
    tags=["Playlists"]
)

@router.post("/create_playlist")
def create_playlist( playlist_data : playlist_create, user_data =Depends(get_current_user),db = Depends(get_db)):

    new_playlist = Playlist(
        user_id = user_data.user_id,
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
def add_song(
    playlist_add_data: playlist_add,
    db=Depends(get_db)
):
    
    exist_song = db.scalar(
        select(playlist_song).where(
            playlist_song.playlist_id == playlist_add_data.playlist_id,
            playlist_song.song_id == playlist_add_data.song_id
        )
    )

    if exist_song:
        raise HTTPException(
            status_code=400,
            detail="Song already exists in playlist"
        )

    new_song = playlist_song(
        playlist_id=playlist_add_data.playlist_id,
        song_id=playlist_add_data.song_id,
        position=playlist_add_data.position
    )

    db.add(new_song)
    db.commit()
    db.refresh(new_song)

    return {
        "message": "Song added successfully",
        "playlist_id": new_song.playlist_id,
        "song_id": new_song.song_id
    }