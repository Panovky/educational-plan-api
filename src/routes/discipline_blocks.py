from fastapi import APIRouter, status, Path
from fastapi.responses import Response
from sqlalchemy import select
from typing import Annotated, Any
from src.dependencies import SessionDep
from src.exceptions import DisciplineBlockNotFoundException
from src.models import DisciplineBlock
from src.schemas import DisciplineBlockCreate, DisciplineBlockUpdate, DisciplineBlockRead

router = APIRouter(
    prefix='/discipline-blocks',
    tags=['discipline blocks']
)


@router.get(
    '/{discipline_block_id}',
    responses={
        200: {'description': 'Discipline block successfully received'},
        404: {'description': 'Discipline block not found'}
    },
    summary='Return the discipline block'
)
def get_discipline_block(discipline_block_id: Annotated[int, Path(gt=0)], session: SessionDep) -> DisciplineBlockRead:
    """Return the discipline block with the specified id"""
    discipline_block = session.get(DisciplineBlock, discipline_block_id)
    if not discipline_block:
        raise DisciplineBlockNotFoundException()
    return discipline_block


@router.patch(
    '/{discipline_block_id}',
    responses={
        200: {'description': 'Discipline block successfully updated'},
        404: {'description': 'Discipline block not found'}
    },
    summary='Update the discipline block'
)
def update_discipline_block(
        discipline_block_id: Annotated[int, Path(gt=0)],
        discipline_block_data: DisciplineBlockUpdate,
        session: SessionDep
) -> DisciplineBlockRead:
    """Update the discipline block with the specified id with the given information (blank values are ignored)"""
    discipline_block = session.get(DisciplineBlock, discipline_block_id)
    if not discipline_block:
        raise DisciplineBlockNotFoundException()
    for key, value in discipline_block_data.model_dump(exclude_none=True).items():
        setattr(discipline_block, key, value)
    session.commit()
    session.refresh(discipline_block)
    return discipline_block


@router.delete(
    '/{discipline_block__id}',
    status_code=status.HTTP_204_NO_CONTENT,
    responses={
        204: {'description': 'Discipline block successfully deleted'},
        404: {'description': 'Discipline block not found'},
    },
    summary='Delete the discipline block'
)
def delete_discipline_block(discipline_block_id: Annotated[int, Path(gt=0)], session: SessionDep) -> Response:
    """Delete the discipline block with the specified id."""
    discipline_block = session.get(DisciplineBlock, discipline_block_id)
    if not discipline_block:
        raise DisciplineBlockNotFoundException()
    session.delete(discipline_block)
    session.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.get(
    '/',
    responses={200: {'description': 'Discipline blocks successfully received'}},
    summary='Return a list of discipline blocks'
)
def get_discipline_blocks(session: SessionDep, limit: int = 10, offset: int = 0) -> list[DisciplineBlockRead]:
    """Return a list of discipline blocks of a given length (limit), starting from a given table entry (offset)."""
    discipline_blocks = session.execute(select(DisciplineBlock).offset(offset).limit(limit)).scalars()
    return discipline_blocks


@router.post(
    '/',
    response_model=DisciplineBlockRead,
    status_code=status.HTTP_201_CREATED,
    responses={201: {'description': 'Discipline block successfully created'}},
    summary='Create the discipline block'
)
def create_discipline_block(discipline_block_data: DisciplineBlockCreate, session: SessionDep) -> Any:
    """Create the discipline block with the given information."""
    discipline_block = DisciplineBlock(**discipline_block_data.model_dump())
    session.add(discipline_block)
    session.commit()
    session.refresh(discipline_block)
    return discipline_block
