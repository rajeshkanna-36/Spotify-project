
from fastapi import FastAPI

from app.database.base import Base
from app.database.connection import engine

from app.models import *

from app.routes.auth import router as auth_router
from app.routes.song import router as song_router
from app.routes.album import router as album_router
from app.routes.artist import router as artist_router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title = "Spotify API",
    version="1.0.0"
)
app.include_router(auth_router)
app.include_router(song_router)
app.include_router(album_router)
app.include_router(artist_router)

