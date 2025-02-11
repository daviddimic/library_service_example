from fastapi import FastAPI
from database import init_db
import api

app = FastAPI()

@app.on_event("startup")
def on_startup():
    init_db()

app.include_router(api.router)

