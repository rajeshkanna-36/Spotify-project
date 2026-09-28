from pydantic import BaseModel
from datetime import datetime

class playlist_create(BaseModel):
  
    playlist_name:str
    created_at:datetime

class playlist_add(BaseModel):
    playlist_id:int
    song_id:int
    position:int
