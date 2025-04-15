from sqlmodel import SQLModel, Field
from sqlalchemy import Column, String


class Favourites(SQLModel, table=True):
    id: int | None = Field(primary_key=True, default=None)
    idspotify: str
    iduser: int
