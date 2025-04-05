from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.routes import disciplines, control_types, directions, discipline_blocks, validations


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['http://localhost:3000', 'http://127.0.0.1:3000', 'http://host.docker.internal:3000'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

app.include_router(disciplines.router)
app.include_router(control_types.router)
app.include_router(directions.router)
app.include_router(discipline_blocks.router)
app.include_router(validations.router)
