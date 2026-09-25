from pydantic import BaseModel

class SongCreate(BaseModel):

    song_name : str
    album_id : int
    song_key : str
    song_cover_key : str
    duration_ms : int