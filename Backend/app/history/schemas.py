from pydantic import BaseModel

class add_history(BaseModel):
    user_id : int
    song_id : int