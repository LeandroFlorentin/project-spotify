from pydantic import BaseModel


class BodyLogin(BaseModel):
    username: str
    password: str


class Data(BaseModel):
    id: int
    username: str
    email: str
    role: str
    access_token: str


class Response(BaseModel):
    status: int
    message: str
    data: Data
