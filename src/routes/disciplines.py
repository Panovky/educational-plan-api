from fastapi import APIRouter, status, Path
from fastapi.responses import Response
from sqlalchemy import select, exists, and_
from typing import Annotated, Any
from src.dependencies import SessionDep
from src.exceptions import (
    DisciplineNotFoundException, DisciplineNameIsNotUniqueException, DisciplineShortNameIsNotUniqueException
)
from src.models import Discipline
from src.schemas import DisciplineCreate, DisciplineUpdate, DisciplineRead

router = APIRouter(
    prefix='/disciplines',
    tags=['disciplines']
)


@router.get(
    '/{discipline_id}',
    responses={200: {'description': 'Discipline successfully received'}, 404: {'description': 'Discipline not found'}},
    summary='Return the discipline'
)
def get_discipline(discipline_id: Annotated[int, Path(gt=0)], session: SessionDep) -> DisciplineRead:
    """Return the discipline with the specified id"""
    discipline = session.get(Discipline, discipline_id)
    if not discipline:
        raise DisciplineNotFoundException()
    return discipline


@router.patch(
    '/{discipline_id}',
    responses={
        200: {'description': 'Discipline successfully updated'},
        404: {'description': 'Discipline not found'},
        409: {'description': 'Discipline data is not unique'}
    },
    summary='Update the discipline'
)
def update_discipline(
        discipline_id: Annotated[int, Path(gt=0)], discipline_data: DisciplineUpdate, session: SessionDep
) -> DisciplineRead:
    """Update the discipline with the specified id with the given information (blank values are ignored)"""
    discipline = session.get(Discipline, discipline_id)
    if not discipline:
        raise DisciplineNotFoundException()

    if discipline_data.name:
        stmt = select(exists().where(and_(Discipline.name == discipline_data.name, Discipline.id != discipline_id)))
        if session.execute(stmt).scalar():
            raise DisciplineNameIsNotUniqueException()

    if discipline_data.short_name:
        stmt = select(exists().where(and_(
            Discipline.short_name == discipline_data.short_name, Discipline.id != discipline_id
        )))
        if session.execute(stmt).scalar():
            raise DisciplineShortNameIsNotUniqueException()

    for key, value in discipline_data.model_dump(exclude_none=True).items():
        setattr(discipline, key, value)
    session.commit()
    session.refresh(discipline)
    return discipline


@router.delete(
    '/{discipline_id}',
    status_code=status.HTTP_204_NO_CONTENT,
    responses={
        204: {'description': 'Discipline successfully deleted'},
        404: {'description': 'Discipline not found'},
    },
    summary='Delete the discipline'
)
def delete_discipline(discipline_id: Annotated[int, Path(gt=0)], session: SessionDep) -> Response:
    """Delete the discipline with the specified id."""
    discipline = session.get(Discipline, discipline_id)
    if not discipline:
        raise DisciplineNotFoundException()
    session.delete(discipline)
    session.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.get(
    '/',
    responses={200: {'description': 'Disciplines successfully received'}},
    summary='Return a list of disciplines'
)
def get_disciplines(session: SessionDep) -> list[DisciplineRead]:
    """Return a list of disciplines."""
    disciplines = session.execute(select(Discipline)).scalars()
    return disciplines


@router.post(
    '/',
    response_model=DisciplineRead,
    status_code=status.HTTP_201_CREATED,
    responses={
        201: {'description': 'Discipline successfully created'},
        409: {'description': 'Discipline data is not unique'}
    },
    summary='Create the discipline'
)
def create_discipline(discipline_data: DisciplineCreate, session: SessionDep) -> Any:
    """Create the discipline with the given information."""

    stmt = select(exists().where(Discipline.name == discipline_data.name))
    if session.execute(stmt).scalar():
        raise DisciplineNameIsNotUniqueException()

    stmt = select(exists().where(Discipline.short_name == discipline_data.short_name))
    if session.execute(stmt).scalar():
        raise DisciplineShortNameIsNotUniqueException()

    discipline = Discipline(**discipline_data.model_dump())
    session.add(discipline)
    session.commit()
    session.refresh(discipline)
    return discipline
