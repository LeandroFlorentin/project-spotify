from pydantic import BaseModel


class Body_add_favourite(BaseModel):
    idspotify: str
    title: str
    artist: str
    album: str
    year: int
    url_image: str
