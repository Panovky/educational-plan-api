from src.directions.repository import DirectionsRepository
from src.map_cors.repository import MapCorsRepository
from src.direction_map_cors.repository import DirectionMapCorsRepository
from src.discipline_blocks.repository import DisciplineBlocksRepository
from src.discipline_block_competencies.repository import DisciplineBlockCompetenciesRepository
from .schemas import MapLoad, MapUnload
from src.exceptions import DirectionNotFoundException


class MapsService:
    def __init__(
            self,
            directions_repository: DirectionsRepository,
            map_cors_repository: MapCorsRepository,
            direction_map_cors_repository: DirectionMapCorsRepository,
            discipline_blocks_repository: DisciplineBlocksRepository,
            discipline_block_competencies_repository: DisciplineBlockCompetenciesRepository,
    ):
        self.directions_repository: DirectionsRepository = directions_repository
        self.map_cors_repository: MapCorsRepository = map_cors_repository
        self.direction_map_cors_repository: DirectionMapCorsRepository = direction_map_cors_repository
        self.discipline_blocks_repository: DisciplineBlocksRepository = discipline_blocks_repository
        self.discipline_block_competencies_repository: DisciplineBlockCompetenciesRepository = \
            discipline_block_competencies_repository

    def load(self, direction_id: int, data: MapLoad) -> None:

        if not self.directions_repository.get_by_id(direction_id):
            raise DirectionNotFoundException()

        for map_core in data.map_cors:

            map_core_id = map_core.id
            if not map_core_id:
                map_core_id = self.map_cors_repository.create({
                    'name': map_core.name,
                    'semesters_count': map_core.semesters_count
                }).id

            self.direction_map_cors_repository.create({
                'direction_id': direction_id,
                'map_core_id': map_core_id
            })

            for discipline_block in map_core.discipline_blocks:
                discipline_block_id = self.discipline_blocks_repository.create({
                    'discipline_id': discipline_block.discipline_id,
                    'credit_units': discipline_block.credit_units,
                    'control_type_id': discipline_block.control_type_id,
                    'lecture_hours': discipline_block.lecture_hours,
                    'practice_hours': discipline_block.practice_hours,
                    'lab_hours': discipline_block.lab_hours,
                    'semester_number': discipline_block.semester_number,
                    'map_core_id': map_core_id
                }).id

                for competency in discipline_block.competencies:
                    self.discipline_block_competencies_repository.create({
                        'discipline_block_id': discipline_block_id,
                        'competency_id': competency.id
                    })

    def unload(self, direction_id) -> MapUnload:
        pass
