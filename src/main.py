from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.routes import (
    educational_levels, educational_forms, directions, activity_types, control_types, departments, disciplines,
    competency_groups, competencies, indicators, map_cors, discipline_blocks, discipline_block_competencies, validations
)


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['http://localhost:3000', 'http://127.0.0.1:3000', 'http://host.docker.internal:3000'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

app.include_router(educational_levels.router)
app.include_router(educational_forms.router)
app.include_router(directions.router)
app.include_router(activity_types.router)
app.include_router(control_types.router)
app.include_router(departments.router)
app.include_router(disciplines.router)
app.include_router(competency_groups.router)
app.include_router(competencies.router)
app.include_router(indicators.router)
app.include_router(map_cors.router)
app.include_router(discipline_blocks.router)
app.include_router(discipline_block_competencies.router)
app.include_router(validations.router)
