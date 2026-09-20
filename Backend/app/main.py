from fastapi import FastAPI

from app.database.base import Base
from app.database.connection import engine
from app.models.user import User

app = FastAPI()

Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
    return {"message": "Hello World"}