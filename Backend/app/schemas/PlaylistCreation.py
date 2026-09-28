from pydantic import BaseModel
from datetime import datetime

class playlist_create(BaseModel):
    user_id:int
    playlist_name:str
    created_at:datetime

class playlist_add(BaseModel):
    playlist_id:int
    song_id:int
    position:int
    