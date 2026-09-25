from pydantic import BaseModel

class add_album(BaseModel):

    album_name : str
    album_cover_key : str