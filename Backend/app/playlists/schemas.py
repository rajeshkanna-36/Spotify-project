from pydantic import BaseModel
from datetime import datetime

class playlist_add(BaseModel):
    playlist_id:int
    song_id:int
    position:int
