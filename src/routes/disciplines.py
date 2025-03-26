from fastapi import APIRouter, status, Path
from fastapi.responses import Response
from sqlalchemy import select
from typing import Annotated, Any
from src.dependencies import SessionDep
from src.exceptions import DisciplineNotFoundException
from src.models import Discipline
from src.schemas import DisciplineBase, DisciplineRead

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
    responses={200: {'description': 'Discipline successfully updated'}, 404: {'description': 'Discipline not found'}},
    summary='Update the discipline'
)
def update_discipline(
        discipline_id: Annotated[int, Path(gt=0)], discipline_data: DisciplineBase, session: SessionDep
) -> DisciplineRead:
    """Update the discipline with the specified id with the given information (blank values are ignored)"""
    discipline = session.get(Discipline, discipline_id)
    if not discipline:
        raise DisciplineNotFoundException()
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
def get_disciplines(session: SessionDep, limit: int = 10, offset: int = 0) -> list[DisciplineRead]:
    """Return a list of disciplines of a given length (limit), starting from a given table entry (offset)."""
    disciplines = session.execute(select(Discipline).offset(offset).limit(limit)).scalars()
    return disciplines


@router.post(
    '/',
    response_model=DisciplineRead,
    status_code=status.HTTP_201_CREATED,
    responses={201: {'description': 'Discipline successfully created'}},
    summary='Create the discipline'
)
def create_discipline(discipline_data: DisciplineBase, session: SessionDep) -> Any:
    """Create the discipline with the given information."""
    discipline = Discipline(**discipline_data.model_dump())
    session.add(discipline)
    session.commit()
    session.refresh(discipline)
    return discipline

