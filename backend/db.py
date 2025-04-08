from fastapi import HTTPException
from sqlmodel import Session, SQLModel, create_engine
from models import models
import os

env = dict(os.environ)

engine = create_engine(env["DATABASE_URL"])


def get_session():
    try:
        with Session(engine) as session:
            yield session
    except Exception as e:
        print("Error accediendo a la base de datos:", e)
        raise HTTPException(
            status_code=500, detail="Error al conectar con la base de datos."
        )


def create_table():
    SQLModel.metadata.create_all(engine)
