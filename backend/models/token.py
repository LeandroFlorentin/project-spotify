from sqlmodel import SQLModel, Field


class Token(SQLModel, table=True):
    id: int | None = Field(primary_key=True, default=None)
    token: str
    expired_in: str
