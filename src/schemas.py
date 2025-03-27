from pydantic import BaseModel, Field
from typing import Annotated


class DisciplineBase(BaseModel):
    name: Annotated[str, Field(example='Проектный практикум', max_length=255)]
    short_name: Annotated[str, Field(example="ПП", max_length=50)]


class DisciplineRead(DisciplineBase):
    id: Annotated[int, Field(example=1)]
