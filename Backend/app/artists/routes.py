from genericpath import exists
from fastapi import Depends, APIRouter,HTTPException

from app.database.connection import get_db
from app.artists.models import artist
from app.artists.schemas import add_artist
from sqlalchemy import select
from app.auth.dependency import get_current_admin
from app.auth.checker import check_admin
from app.artists.models import song_artist

router = APIRouter(
    prefix="/artist",
    tags=["Artist"]
)


@router.post("/add_artist")
def add_artist(artist_data: add_artist,admin=Depends(get_current_admin), db=Depends(get_db)):
    
    check_admin(admin.admin_id, db)

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

@router.delete("/delete_artist/{artist_id}")
def delete_artist(
    artist_id: int,
    admin=Depends(get_current_admin),
    db=Depends(get_db)
):
    check_admin(admin.admin_id, db)

    exist_artist = db.scalar(
        select(artist).where(
            artist.artist_id == artist_id
        )
    )

    if not exist_artist:
        raise HTTPException(
            status_code=404,
            detail="Artist not found"
        )

    # Delete artist ↔ song relationships
    db.query(song_artist).filter(
        song_artist.artist_id == artist_id
    ).delete()

    # Delete artist
    db.delete(exist_artist)

    db.commit()

    return {
        "message": "Artist deleted",
        "artist_id": artist_id
    }