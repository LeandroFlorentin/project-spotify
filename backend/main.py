from fastapi import FastAPI
from dotenv import load_dotenv
from routes import main_router

load_dotenv()

from db import create_table
import os


env = dict(os.environ)
port = env["PORT"]

app = FastAPI()

app.include_router(main_router)

create_table()


@app.on_event("startup")
def life_span():
    create_table()
