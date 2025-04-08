from dotenv import load_dotenv

load_dotenv()

from fastapi import FastAPI
from routes import main_router
from db import create_table

app = FastAPI()

app.include_router(main_router)


@app.on_event("startup")
def life_span():
    create_table()
