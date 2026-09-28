from fastapi import Depends, APIRouter

from app.database.connection import get_db
from app.artists.models import artist
from app.artists.schemas import add_artist
from sqlalchemy import select

router = APIRouter(
    prefix="/artist",
    tags=["Artist"]
)


@router.post("/add_artist")
async def add_artist(artist_data: add_artist, db=Depends(get_db)):

    new_artist = artist(
        artist_name=artist_data.artist_name
    )

    db.add(new_artist)
    db.commit()
    db.refresh(new_artist)

    return {
        "message": "Artist added",
        "artist_id": new_artist.artist_id
    }
