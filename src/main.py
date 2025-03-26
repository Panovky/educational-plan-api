from fastapi import FastAPI
from src.routes import disciplines


app = FastAPI()

app.include_router(disciplines.router)
