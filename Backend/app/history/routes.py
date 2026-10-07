from fastapi import APIRouter,Depends,HTTPException, Query
from sqlalchemy import select

from app.database.connection import get_db
from app.songs.models import SongDetails
from app.history.models import history
from app.history.schemas import add_history
from app.auth.dependency import get_current_user
from app.auth.checker import check_user

router = APIRouter(
    prefix="/history",
    tags=["History"]    
)


@router.post("/add_history")
def add_history(
    history_data: add_history,
    user_data=Depends(get_current_user),
    db=Depends(get_db)
):
    check_user(user_data.user_id, db)
    check_song = db.scalar(
        select(SongDetails).where(
            SongDetails.song_id == history_data.song_id
        )
    )
    if not check_song:
        raise HTTPException(
            status_code=404,
            detail="Song not found"
        )
    new_history = history(
        user_id=user_data.user_id,
        song_id=history_data.song_id
    )
    db.add(new_history)
    db.commit()
    db.refresh(new_history)
    return new_history

@router.get("/my_history")
def get_history(page_no : int = Query(1, ge=1),limit : int = Query(10, ge=1, le=100) ,user_data=Depends(get_current_user), db=Depends(get_db)):
    check_user(user_data.user_id, db)

    offset = (page_no - 1) * limit


    histories = db.scalars(
        select(history).where(
            history.user_id == user_data.user_id
        ).order_by(history.played_at.desc()).limit(limit).offset(offset)
    ).all()

    return histories


@router.delete("/all")
def delete_all_history(user_data=Depends(get_current_user), db=Depends(get_db)):
    check_user(user_data.user_id, db)
    db.query(history).filter(
        history.user_id == user_data.user_id
    ).delete()
    db.commit()
    return {
        "message": "History deleted successfully"
    }
    

@router.delete("/{history_id}")
def delete_history(history_id:int, user_data=Depends(get_current_user), db=Depends(get_db)):
    check_user(user_data.user_id, db)
    check_history = db.scalar(
        select(history).where(
            history.history_id == history_id
        )
    )
    if not check_history:
        raise HTTPException(
            status_code=404,
            detail="History not found"
        )
    db.delete(check_history)
    db.commit()
    return {
        "message": "History deleted successfully"
    }

