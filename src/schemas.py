from pydantic import BaseModel, Field
from typing import Annotated


class DisciplineCreate(BaseModel):
    name: Annotated[str, Field(example='Проектный практикум', max_length=255)]
    short_name: Annotated[str, Field(example="ПП", max_length=50)]


class DisciplineUpdate(BaseModel):
    name: Annotated[str | None, Field(example='Проектный практикум', max_length=255)]
    short_name: Annotated[str | None, Field(example="ПП", max_length=50)]


class DisciplineRead(DisciplineCreate):
    id: Annotated[int, Field(example=1)]


class DirectionCreate(BaseModel):
    name: Annotated[str, Field(example='Программная инженерия', max_length=50)]
    educational_level_id: Annotated[int, Field(example=1)]
    educational_form_id: Annotated[int, Field(example=1)]
    semester_count: Annotated[int, Field(example=8)]


class DirectionUpdate(BaseModel):
    name: Annotated[str  | None, Field(example='Программная инженерия', max_length=50)]
    educational_level_id: Annotated[int | None, Field(example=1)]
    educational_form_id: Annotated[int | None, Field(example=1)]
    semester_count: Annotated[int | None, Field(example=8)]


class DirectionRead(DirectionCreate):
    id: Annotated[int, Field(example=1)]


class DisciplineBlockCreate(BaseModel):
    discipline_id: Annotated[int, Field(example=1)]
    credit_units: Annotated[int, Field(example=3)]
    control_type_id: Annotated[int, Field(example=1)]
    department_id: Annotated[int, Field(example=1)]
    lecture_hours: Annotated[int, Field(example=40)]
    practice_hours: Annotated[int, Field(example=40)]
    lab_hours: Annotated[int, Field(example=40)]
    semester_number: Annotated[int, Field(example=3)]
    map_core_id: Annotated[int, Field(example=1)]
    direction_id: Annotated[int, Field(example=1)]


class DisciplineBlockUpdate(BaseModel):
    discipline_id: Annotated[int | None, Field(example=1)]
    credit_units: Annotated[int | None, Field(example=3)]
    control_type_id: Annotated[int | None, Field(example=1)]
    department_id: Annotated[int | None, Field(example=1)]
    lecture_hours: Annotated[int | None, Field(example=40)]
    practice_hours: Annotated[int | None, Field(example=40)]
    lab_hours: Annotated[int | None, Field(example=40)]
    semester_number: Annotated[int | None, Field(example=3)]
    map_core_id: Annotated[int | None, Field(example=1)]
    direction_id: Annotated[int | None, Field(example=1)]


class DisciplineBlockRead(DisciplineBlockCreate):
    id: Annotated[int, Field(example=1)]


