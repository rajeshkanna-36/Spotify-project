from fastapi import Depends, APIRouter

from app.database.connection import get_db
from app.models.artist import artist
from app.schemas.ArtistCreation import ArtistCreate
from sqlalchemy import select

router = APIRouter(
    prefix="/artist",
    tags=["Artist"]
)


@router.post("/add_artist")
def add_artist(artist_data: ArtistCreate, db=Depends(get_db)):

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