from sqlmodel import SQLModel, Field
from sqlalchemy import Column, String, JSON
from datetime import datetime
from typing import Any


def current_datetime():
    return datetime.now().strftime("%d-%m-%Y %H:%M:%S")


class Song(SQLModel, table=True):
    idsong: int | None = Field(default=None, primary_key=True)
    idspotify: str = Field(index=True)
    title: str = Field(index=True)
    artist: dict[str, Any] = Field(sa_column=Column(JSON))
    album: dict[str, Any] = Field(sa_column=Column(JSON))
    duration: str = Field(index=True)
    created_at: str = Field(default_factory=current_datetime)
    last_updated: str | None = Field(default=None)
