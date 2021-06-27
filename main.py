# main.py
from fastapi import FastAPI, HTTPException

from sqlalchemy.orm import Session

import models, schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)


app = FastAPI()

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

@app.get("/")
def read_root():
    return {"Hello": "World"}
