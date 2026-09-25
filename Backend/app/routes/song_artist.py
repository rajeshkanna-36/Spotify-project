from fastapi import Depends, HTTPException, APIRouter
from sqlalchemy import select

from app.models.song_artist import song_artist
from app.schemas.SongArtistCreation import add_song_artist
from app.models import artist, SongDetails
from app.database.connection import get_db


router = APIRouter(
    prefix="/song_artist",
    tags=["Song Artist"]
)


@router.post("/add_song_artist")
def add_song_artist(
    song_artist_data: add_song_artist,
    db=Depends(get_db)
):

    check_artist = db.scalar(
        select(artist).where(
            artist.artist_id == song_artist_data.artist_id
        )
    )

    check_song = db.scalar(
        select(SongDetails).where(
            SongDetails.song_id == song_artist_data.song_id
        )
    )

    if not check_artist:
        raise HTTPException(
            status_code=404,
            detail="Artist not found"
        )

    if not check_song:
        raise HTTPException(
            status_code=404,
            detail="Song not found"
        )

    new_song_artist = song_artist(
        song_id=song_artist_data.song_id,
        artist_id=song_artist_data.artist_id
    )

    db.add(new_song_artist)
    db.commit()
    db.refresh(new_song_artist)

    return {
        "message": "Song artist added",
        "song_id": new_song_artist.song_id,
        "artist_id": new_song_artist.artist_id
    }