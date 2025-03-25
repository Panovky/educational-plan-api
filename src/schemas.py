from pydantic import BaseModel, Field
from typing import Annotated


class DisciplineBase(BaseModel):
    name: Annotated[str, Field(example='Проектный практикум', max_length=255)]


class DisciplineRead(DisciplineBase):
    id: Annotated[int, Field(example=1)]
