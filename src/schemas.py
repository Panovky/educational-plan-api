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
