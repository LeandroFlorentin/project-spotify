from sqlmodel import SQLModel, Field
from datetime import datetime


def current_datetime():
    return datetime.now().strftime("%d-%m-%Y %H:%M:%S")


class Song(SQLModel, table=True):
    idsong: int | None = Field(default=None, primary_key=True)
    idspotify: str = Field(index=True)
    title: str = Field(index=True)
    artist: str = Field(index=True)
    album: str = Field(index=True)
    duration: int = Field(index=True)
    genre: str = Field(index=True)
    year: int = Field(index=True)
    url_image: str = Field(index=True)
    created_at: str = Field(default_factory=current_datetime)
    last_updated: str | None = Field(default=None)
