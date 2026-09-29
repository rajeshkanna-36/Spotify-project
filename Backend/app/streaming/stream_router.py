from fastapi import APIRouter, Depends, HTTPException, Request
from fastapi.responses import StreamingResponse
from sqlalchemy import select

from app.auth.dependency import get_current_user
from app.database.connection import get_db
from app.songs.models import SongDetails
from app.storage.s3 import s3_client
from app.core.settings import AWS_S3_BUCKET


router = APIRouter(
    prefix="/stream",
    tags=["Streaming"]
)


@router.get("/song/{song_id}")
def stream_song(
    song_id: int,
    request: Request,
    user_data=Depends(get_current_user),
    db=Depends(get_db)
):
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

    # Get requested byte range
    range_header = request.headers.get("range")

    # Get file size from S3
    head = s3_client.head_object(
        Bucket=AWS_S3_BUCKET,
        Key=song.song_key
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