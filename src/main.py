from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.routes import disciplines, validations


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['http://localhost:3000', 'http://127.0.0.1:3000'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

app.include_router(disciplines.router)
app.include_router(validations.router)
