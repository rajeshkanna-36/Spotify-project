from fastapi import APIRouter,Depends,HTTPException

from app.playlists.models import Playlist, playlist_song
from app.playlists.schemas import playlist_create, playlist_add
from app.database.connection import get_db
from app.auth.dependency import get_current_user
from sqlalchemy import select
from app.auth.checker import check_user

router = APIRouter(
    prefix="/playlist",
    tags=["Playlists"]
)

@router.post("/create_playlist")
def create_playlist( playlist_data : playlist_create, user_data =Depends(get_current_user),db = Depends(get_db)):

    check_user(user_data.user_id)
    
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
    playlist_add_data: playlist_add,user_data =Depends(get_current_user),db=Depends(get_db)):

    check_user(user_data.user_id)
    
    playlist = db.scalar(
        select(Playlist).where(
            Playlist.playlist_id == playlist_add_data.playlist_id,
            Playlist.user_id == user_data.user_id
        )
    )

    if not playlist:
        raise HTTPException(
            status_code=404,
            detail="Playlist not found"
        )

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

@router.get("/my_playlist")
def my_playlist(user_data = Depends(get_current_user),db = Depends(get_db)):
    check_user(user_data.user_id)
    
    playlists = db.scalars(
        select(Playlist).where(
            Playlist.user_id == user_data.user_id
        )
    ).all()
    return playlists

@router.get("/{playlist_id}")
def playlist(playlist_id: int,user_data = Depends(get_current_user),db = Depends(get_db)):
    playlist = db.scalar(
        select(Playlist).where(
            Playlist.playlist_id == playlist_id,
            Playlist.user_id == user_data.user_id
        )
    )
    if not playlist:
        raise HTTPException(
            status_code=404,
            detail="Playlist not found"
        )
    return playlist

@router.delete("/{playlist_id}")
def delete_playlist(playlist_id:int,user_data = Depends(get_current_user),db = Depends(get_db)):
    
    check_user(user_data.user_id)
    
    playlist = db.scalar(
        select(Playlist).where(
            Playlist.playlist_id == playlist_id,
            Playlist.user_id == user_data.user_id
        )
    )
    if not playlist:
        raise HTTPException(
            status_code=404,
            detail="Playlist not found"
        )
    db.delete(playlist)
    db.commit()
    return {
        "message": "Playlist deleted successfully"
    }

@router.get("/{playlist_id}/songs")
def playlist_songs(playlist_id:int,user_data = Depends(get_current_user),db = Depends(get_db)):
    
    check_user(user_data.user_id)
    
    playlist = db.scalar(
        select(Playlist).where(
            Playlist.playlist_id == playlist_id,
            Playlist.user_id == user_data.user_id
        )
    )
    if not playlist:
        raise HTTPException(
            status_code=404,
            detail="Playlist not found"
        )
    songs = db.scalars(
        select(playlist_song).where(
            playlist_song.playlist_id == playlist_id
        )
    ).all()
    return songs


@router.delete("/{playlist_id}/song/{song_id}")
def delete_song(playlist_id:int,song_id:int,user_data = Depends(get_current_user),db = Depends(get_db)):
    
    check_user(user_data.user_id)
    
    playlist = db.scalar(
        select(Playlist).where(
            Playlist.playlist_id == playlist_id,
            Playlist.user_id == user_data.user_id
        )
    )
    if not playlist:
        raise HTTPException(
            status_code=404,
            detail="Playlist not found"
        )
    song = db.scalar(
        select(playlist_song).where(
            playlist_song.playlist_id == playlist_id,
            playlist_song.song_id == song_id
        )
    )
    if not song:
        raise HTTPException(
            status_code=404,
            detail="Song not found in playlist"
        )
    db.delete(song)
    db.commit()
    return {
        "message": "Song deleted successfully from playlist"
    }
