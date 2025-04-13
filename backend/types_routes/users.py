from pydantic import BaseModel
from typing import List, Dict


class BodyUser(BaseModel):
    username: str
    email: str
    password: str
    role: list[str]


class UserData(BaseModel):
    id: int
    username: str
    email: str
    role: List[str]
    disabled: int
    access_token: str


class Response_create(BaseModel):
    status: int
    message: str
    data: UserData


class Data_get(BaseModel):
    id: int
    username: str
    email: str
    role: List[str]
    createdAt: str
    updatedAt: str


class Response_get(BaseModel):
    status: int
    message: str
    data: Data_get


class Generic_response(BaseModel):
    status: int
    message: str
    data: Dict = {}
