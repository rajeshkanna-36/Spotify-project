
from fastapi import FastAPI

from app.database.base import Base
from app.database.connection import engine

# Import all models so SQLAlchemy registers them before create_all
from app.users.models import User
from app.auth.models import SessionTable
from app.admin.model import Admin
from app.songs.models import SongDetails, song_artist
from app.albums.models import album
from app.artists.models import artist
from app.playlists.models import Playlist, playlist_song

from app.auth.routes import router as auth_router
from app.admin.router import router as admin_router
from app.songs.routes import router as song_router
from app.albums.routes import router as album_router
from app.artists.routes import router as artist_router
from app.songs.song_artist_routes import router as song_artist_router
from app.playlists.routes import router as playlist_router
from app.streaming.stream_router import router as stream_router


Base.metadata.create_all(bind=engine)

app = FastAPI(
    title = "Spotify API",
    version="1.0.0"
)
app.include_router(auth_router)
app.include_router(admin_router)
app.include_router(song_router)
app.include_router(album_router)
app.include_router(artist_router)
app.include_router(song_artist_router)
app.include_router(playlist_router)
app.include_router(stream_router)


