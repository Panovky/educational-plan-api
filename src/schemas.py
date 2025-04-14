from pydantic import BaseModel, Field
from typing import Annotated


class ActivityTypeCreate(BaseModel):
    name: Annotated[str, Field(example='Практическое занятие', max_length=30)]


class ActivityTypeUpdate(BaseModel):
    name: Annotated[str | None, Field(example='Практическое занятие', max_length=30)]


class ActivityTypeRead(ActivityTypeCreate):
    id: Annotated[int, Field(example=1)]


class CompetencyCreate(BaseModel):
    code: Annotated[str, Field(example='УК-1', max_length=10)]
    name: Annotated[str, Field(example='Способен осуществлять поиск, критический анализ и синтез информации, '
                                       'применять системный подход для решения поставленных задач.', max_length=255)]
    competency_group_id: Annotated[int, Field(gt=0, example=1)]


class CompetencyUpdate(BaseModel):
    code: Annotated[str | None, Field(example='УК-1', max_length=10)]
    name: Annotated[str | None, Field(example='Способен осуществлять поиск, критический анализ и синтез информации, '
                                              'применять системный подход для решения поставленных задач.',
                                      max_length=255)]
    competency_group_id: Annotated[int | None, Field(gt=0, example=1)]


class CompetencyRead(CompetencyCreate):
    id: Annotated[int, Field(example=1)]


class CompetencyGroupCreate(BaseModel):
    name: Annotated[str, Field(example='Универсальные', max_length=30)]


class CompetencyGroupUpdate(BaseModel):
    name: Annotated[str | None, Field(example='Универсальные', max_length=30)]


class CompetencyGroupRead(CompetencyGroupCreate):
    id: Annotated[int, Field(example=1)]


class ControlTypeCreate(BaseModel):
    name: Annotated[str, Field(example='Дифференцированный зачет', max_length=30)]


class ControlTypeUpdate(BaseModel):
    name: Annotated[str | None, Field(example='Дифференцированный зачет', max_length=30)]


class ControlTypeRead(ControlTypeCreate):
    id: Annotated[int, Field(example=1)]


class DepartmentCreate(BaseModel):
    name: Annotated[str, Field(example='Информационные системы и технологии', max_length=50)]


class DepartmentUpdate(BaseModel):
    name: Annotated[str | None, Field(example='Информационные системы и технологии', max_length=50)]


class DepartmentRead(DepartmentCreate):
    id: Annotated[int, Field(example=1)]


class DirectionCreate(BaseModel):
    name: Annotated[str, Field(example='Программная инженерия', max_length=50)]
    educational_level_id: Annotated[int, Field(example=1)]
    educational_form_id: Annotated[int, Field(example=1)]
    semester_count: Annotated[int, Field(example=8)]


class DirectionUpdate(BaseModel):
    name: Annotated[str | None, Field(example='Программная инженерия', max_length=50)]
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


class DisciplineCreate(BaseModel):
    name: Annotated[str, Field(example='Проектный практикум', max_length=255)]
    short_name: Annotated[str, Field(example="ПП", max_length=50)]


class DisciplineUpdate(BaseModel):
    name: Annotated[str | None, Field(example='Проектный практикум', max_length=255)]
    short_name: Annotated[str | None, Field(example="ПП", max_length=50)]


class DisciplineRead(DisciplineCreate):
    id: Annotated[int, Field(example=1)]


class IndicatorCreate(BaseModel):
    code: Annotated[str, Field(example='УК-1.1', max_length=10)]
    name: Annotated[str, Field(example='Знать: методики поиска, сбора и обработки информации; актуальные российские и '
                                       'зарубежные источники информации в сфере профессиональной деятельности; '
                                       'метод системного анализа.', max_length=255)]
    competency_id: Annotated[int, Field(gt=0, example=1)]


class IndicatorUpdate(BaseModel):
    code: Annotated[str | None, Field(example='УК-1.1', max_length=10)]
    name: Annotated[str | None, Field(example='Знать: методики поиска, сбора и обработки информации; актуальные '
                                              'российские и зарубежные источники информации в сфере профессиональной '
                                              'деятельности; метод системного анализа.', max_length=255)]
    competency_id: Annotated[int | None, Field(gt=0, example=1)]


class IndicatorRead(IndicatorCreate):
    id: Annotated[int, Field(example=1)]
