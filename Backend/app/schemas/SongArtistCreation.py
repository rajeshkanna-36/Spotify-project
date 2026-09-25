from pydantic import BaseModel

class add_song_artist(BaseModel):
    song_id : int
    artist_id : int