from pydantic import BaseModel

class song_search_result(BaseModel):
    song_id: int
    song_name:str
    
class artist_search_result(BaseModel):
    artist_id: int
    artist_name:str
    
class album_search_result(BaseModel):
    album_id: int
    album_name:str

class search_result(BaseModel):
    songs: list[song_search_result]
    artists: list[artist_search_result]
    albums: list[album_search_result]
