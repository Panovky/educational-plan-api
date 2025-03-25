import os
from fastapi import FastAPI
from src.routes import disciplines
from sqlalchemy import create_engine

engine = create_engine(os.getenv('DATABASE_URL'), echo=True)

app = FastAPI()

app.include_router(disciplines.router)
