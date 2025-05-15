from pydantic import BaseModel, Field
from typing import Annotated


class CompetencyLoad(BaseModel):
    id: Annotated[int, Field(gt=0)]


class DisciplineBlockLoad(BaseModel):
    discipline_id: Annotated[int, Field(gt=0)]
    credit_units: Annotated[int, Field(gt=0, example=3)]
    control_type_id: Annotated[int, Field(gt=0)]
    lecture_hours: Annotated[int, Field(gte=0, example=40)]
    practice_hours: Annotated[int, Field(gte=0, example=40)]
    lab_hours: Annotated[int, Field(gte=0, example=40)]
    semester_number: Annotated[int, Field(gt=0)]
    competencies: list[CompetencyLoad]


class MapCoreLoad(BaseModel):
    id: Annotated[int | None, Field(gt=0, default=None)]
    name: Annotated[str, Field(max_length=50, example='Ядро ЯГТУ')]
    semesters_count: Annotated[int, Field(gt=0, example=8)]
    discipline_blocks: list[DisciplineBlockLoad]


class MapLoad(BaseModel):
    direction_id: Annotated[int, Field(gt=0)]
    map_cors: list[MapCoreLoad]


class DepartmentUnload(BaseModel):
    id: Annotated[int, Field(example=1)]
    name: Annotated[str, Field(example='Информационные системы и технологии')]
    short_name: Annotated[str, Field(example='ИСТ')]


class CompetencyUnload(BaseModel):
    id: Annotated[int, Field(example=1)]
    code: Annotated[str, Field(example='УК-3')]
    name: Annotated[str, Field(example='Командная работа и лидерство')]
    description: Annotated[str, Field(
        example='Способен осуществлять социальное взаимодействие и реализовывать свою роль в команде.'
    )]
    competency_group_id: Annotated[int, Field(example=1)]


class DisciplineUnload(BaseModel):
    id: Annotated[int, Field(example=1)]
    name: Annotated[str, Field(example='Проектный практикум')]
    short_name: Annotated[str, Field(example='ПП')]
    department: DepartmentUnload


class ControlTypeUnload(BaseModel):
    id: Annotated[int, Field(example=1)]
    name: Annotated[str, Field(example='Дифференцированный зачет')]


class DisciplineBlockUnload(BaseModel):
    id: Annotated[int, Field(example=1)]
    discipline: DisciplineUnload
    credit_units: Annotated[int, Field(example=3)]
    control_type: ControlTypeUnload
    lecture_hours: Annotated[int, Field(example=40)]
    practice_hours: Annotated[int, Field(example=40)]
    lab_hours: Annotated[int, Field(example=40)]
    semester_number: Annotated[int, Field(example=3)]
    competencies: list[CompetencyUnload]


class MapCoreUnload(BaseModel):
    id: Annotated[int, Field(example=1)]
    name: Annotated[str, Field(example='Ядро ЯГТУ')]
    semesters_count: Annotated[int, Field(example=8)]
    discipline_blocks: list[DisciplineBlockUnload]


class MapUnload(BaseModel):
    map_cors: list[MapCoreUnload]
