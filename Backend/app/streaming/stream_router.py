from datetime import datetime, timezone
from fastapi import APIRouter, Depends, HTTPException, Query, Request
from fastapi.responses import StreamingResponse
from jose import JWTError, jwt
from sqlalchemy import select

from app.database.connection import get_db
from app.songs.models import SongDetails
from app.history.models import history
from app.auth.models import SessionTable
from app.storage.s3 import s3_client
from app.core.settings import AWS_S3_BUCKET, JWT_SECRET_KEY, JWT_ALGORITHM
from app.auth.checker import check_user


router = APIRouter(
    prefix="/stream",
    tags=["Streaming"]
)


def authenticate_stream_token(token: str, db):
    try:
        payload = jwt.decode(
            token,
            JWT_SECRET_KEY,
            algorithms=[JWT_ALGORITHM]
        )
    except JWTError:
        raise HTTPException(
            status_code=401,
            detail="Invalid or expired token"
        )

    if payload.get("type") != "user":
        raise HTTPException(
            status_code=401,
            detail="Invalid user token"
        )

    user_id = int(payload.get("sub"))

    session = db.scalar(
        select(SessionTable).where(
            SessionTable.user_id == user_id,
            SessionTable.token == token,
            SessionTable.expire_at > datetime.now(timezone.utc),
            SessionTable.revoked == False
        )
    )

    if not session:
        raise HTTPException(
            status_code=401,
            detail="Invalid session or token expired"
        )

    return check_user(user_id, db)


@router.get("/song/{song_id}")
def stream_song(
    song_id: int,
    request: Request,
    token: str | None = Query(None, description="JWT access token"),
    db=Depends(get_db)
):  
    # 1. Retrieve token from query param or Authorization header
    raw_token = token
    if not raw_token:
        auth_header = request.headers.get("authorization")
        if auth_header and auth_header.startswith("Bearer "):
            raw_token = auth_header[7:].strip()

    user = None
    if raw_token and raw_token not in ("null", "undefined"):
        try:
            user = authenticate_stream_token(raw_token, db)
        except Exception:
            user = None
    
    # Find song
    song = db.scalar(
        select(SongDetails).where(
            SongDetails.song_id == song_id
        )
    )

    if not song:
        raise HTTPException(
            status_code=404,
            detail="Song not found"
        )

    # Automatically log to recently played history on playback start
    range_header = request.headers.get("range")
    if not range_header or range_header.startswith("bytes=0-"):
        try:
            new_history = history(
                user_id=user.user_id,
                song_id=song_id
            )
            db.add(new_history)
            db.commit()
        except Exception:
            db.rollback()

    # Get requested byte range
    range_header = request.headers.get("range")

    # Get file size from S3
    try:
        head = s3_client.head_object(
            Bucket=AWS_S3_BUCKET,
            Key=song.song_key
        )
    except Exception:
        raise HTTPException(
            status_code=404,
            detail=f"Audio file '{song.song_name}' not found in storage"
        )

    file_size = head["ContentLength"]

    # If browser did not send Range
    if not range_header:
        response = s3_client.get_object(
            Bucket=AWS_S3_BUCKET,
            Key=song.song_key
        )

        body = response["Body"]

        return StreamingResponse(
            body.iter_chunks(chunk_size=1024 * 1024),
            media_type="audio/mpeg",
            headers={
                "Accept-Ranges": "bytes",
                "Content-Length": str(file_size),
            }
        )

    #Parse Range header
    if not range_header.startswith("bytes="):
        raise HTTPException(
            status_code=416,
            detail="Invalid Range header"
        )

    range_value = range_header.replace("bytes=", "")

    try:
        start_str, end_str = range_value.split("-")

        start = int(start_str)

        if end_str:
            end = int(end_str)
        else:
            end = file_size - 1

    except ValueError:
        raise HTTPException(
            status_code=416,
            detail="Invalid Range header"
        )

    #Validate range
    if start >= file_size or start > end:
        raise HTTPException(
            status_code=416,
            detail="Requested range not satisfiable"
        )

    end = min(end, file_size - 1)

    content_length = end - start + 1

    #Ask S3 only for requested bytes
    response = s3_client.get_object(
        Bucket=AWS_S3_BUCKET,
        Key=song.song_key,
        Range=f"bytes={start}-{end}"
    )

    body = response["Body"]

    #Return partial content
    return StreamingResponse(
        body.iter_chunks(chunk_size=1024 * 1024),
        status_code=206,
        media_type="audio/mpeg",
        headers={
            "Accept-Ranges": "bytes",
            "Content-Range": f"bytes {start}-{end}/{file_size}",
            "Content-Length": str(content_length),
        }
    )