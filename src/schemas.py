from pydantic import BaseModel, Field
from typing import Annotated


class DisciplineBase(BaseModel):
    name: Annotated[str, Field(example='Проектный практикум', max_length=255)]
    short_name: Annotated[str, Field(example="ПП", max_length=50)]


class DisciplineRead(DisciplineBase):
    id: Annotated[int, Field(example=1)]


class DirectionBase(BaseModel):
    name: Annotated[str, Field(example='Программная инженерия', max_length=50)]
    educational_level_id: Annotated[int, Field(example=1)]
    educational_form_id: Annotated[int, Field(example=1)]
    semester_count: Annotated[int, Field(example=8)]


class DirectionRead(DirectionBase):
    id: Annotated[int, Field(example=1)]


class DisciplineBlockBase(BaseModel):
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


class DisciplineBlockRead(DisciplineBlockBase):
    id: Annotated[int, Field(example=1)]


