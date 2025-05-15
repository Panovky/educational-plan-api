from fastapi import Depends
from sqlalchemy.orm import Session
from typing import Annotated
from src.database import engine
from src.directions.repository import DirectionsRepository
from src.map_cors.repository import MapCorsRepository
from src.direction_map_cors.repository import DirectionMapCorsRepository
from src.discipline_blocks.repository import DisciplineBlocksRepository
from src.discipline_block_competencies.repository import DisciplineBlockCompetenciesRepository
from src.maps.service import MapsService


def get_session() -> Session:
    with Session(autoflush=False, bind=engine) as session:
        yield session


SessionDep = Annotated[Session, Depends(get_session)]


def get_directions_repository(session: SessionDep) -> DirectionsRepository:
    return DirectionsRepository(session)


DirectionsRepositoryDep = Annotated[DirectionsRepository, Depends(get_directions_repository)]


def get_map_cors_repository(session: SessionDep) -> MapCorsRepository:
    return MapCorsRepository(session)


MapCorsRepositoryDep = Annotated[MapCorsRepository, Depends(get_map_cors_repository)]


def get_direction_map_cors_repository(session: SessionDep) -> DirectionMapCorsRepository:
    return DirectionMapCorsRepository(session)


DirectionMapCorsRepositoryDep = Annotated[DirectionMapCorsRepository, Depends(get_direction_map_cors_repository)]


def get_discipline_blocks_repository(session: SessionDep) -> DisciplineBlocksRepository:
    return DisciplineBlocksRepository(session)


DisciplineBlocksRepositoryDep = Annotated[DisciplineBlocksRepository, Depends(get_discipline_blocks_repository)]


def get_discipline_block_competencies_repository(session: SessionDep) -> DisciplineBlockCompetenciesRepository:
    return DisciplineBlockCompetenciesRepository(session)


DisciplineBlockCompetenciesRepositoryDep = Annotated[
    DisciplineBlockCompetenciesRepository, Depends(get_discipline_block_competencies_repository)
]


def get_maps_service(
        directions_repository: DirectionsRepositoryDep,
        map_cors_repository: MapCorsRepositoryDep,
        direction_map_cors_repository: DirectionMapCorsRepositoryDep,
        discipline_blocks_repository: DisciplineBlocksRepositoryDep,
        discipline_block_competencies_repository: DisciplineBlockCompetenciesRepositoryDep,
) -> MapsService:
    return MapsService(
        directions_repository,
        map_cors_repository,
        direction_map_cors_repository,
        discipline_blocks_repository,
        discipline_block_competencies_repository,
    )


MapsServiceDep = Annotated[MapsService, Depends(get_maps_service)]
