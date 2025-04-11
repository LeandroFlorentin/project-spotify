from sqlmodel import SQLModel, Field
from datetime import datetime


class Token(SQLModel, table=True):
    id: int | None = Field(primary_key=True, default=None)
    token: str
    expires_in: datetime
