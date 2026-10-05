from sqlalchemy import select
from fastapi import APIRouter,Depends
from app.database.connection import get_db
from app.auth.dependency import get_current_user
from app.auth.checker import check_user
from app.songs.models import SongDetails
from app.artists.models import artist
from app.albums.models import album



router = APIRouter(
    prefix="/search",
    tags=["Search"]
)
@router.get("/")
def search(q:str, user_data = Depends(get_current_user),db = Depends(get_db)):
    check_user(user_data.user_id, db)

    songs = db.scalars(
        select(SongDetails).where(
            SongDetails.song_name.ilike(f"%{q}%")
        ).limit(5)
    ).all()

    artist_data = db.scalars(
        select(artist).where(
            artist.artist_name.ilike(f"%{q}%")
        ).limit(5)
    ).all()

    album_data = db.scalars(
        select(album).where(
            album.album_name.ilike(f"%{q}%")
        ).limit(5)
    ).all()

    
    return {"Songs" : songs,"Artist":artist_data,"Album":album_data}
    