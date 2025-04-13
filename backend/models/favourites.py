from sqlmodel import SQLModel, Field


class Favourites(SQLModel, table=True):
    id: int | None = Field(primary_key=True, default=None)
    idsong: str
    iduser: int
