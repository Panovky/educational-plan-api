from fastapi import APIRouter, status, Path
from fastapi.responses import Response
from sqlalchemy import select
from typing import Annotated, Any
from src.dependencies import SessionDep
from src.exceptions import DirectionNotFoundException
from src.models import Direction
from src.schemas import DirectionCreate, DirectionUpdate, DirectionRead

router = APIRouter(
    prefix='/directions',
    tags=['directions']
)


@router.get(
    '/{direction_id}',
    responses={200: {'description': 'Direction successfully received'}, 404: {'description': 'Direction not found'}},
    summary='Return the direction'
)
def get_direction(direction_id: Annotated[int, Path(gt=0)], session: SessionDep) -> DirectionRead:
    """Return the direction with the specified id"""
    direction = session.get(Direction, direction_id)
    if not direction:
        raise DirectionNotFoundException()
    return direction


@router.patch(
    '/{direction_id}',
    responses={200: {'description': 'Direction successfully updated'}, 404: {'description': 'Direction not found'}},
    summary='Update the direction'
)
def update_direction(
        direction_id: Annotated[int, Path(gt=0)], direction_data: DirectionUpdate, session: SessionDep
) -> DirectionRead:
    """Update the direction with the specified id with the given information (blank values are ignored)"""
    direction = session.get(Direction, direction_id)
    if not direction:
        raise DirectionNotFoundException()
    for key, value in direction_data.model_dump(exclude_none=True).items():
        setattr(direction, key, value)
    session.commit()
    session.refresh(direction)
    return direction


@router.delete(
    '/{direction_id}',
    status_code=status.HTTP_204_NO_CONTENT,
    responses={
        204: {'description': 'Direction successfully deleted'},
        404: {'description': 'Direction not found'},
    },
    summary='Delete the direction'
)
def delete_direction(direction_id: Annotated[int, Path(gt=0)], session: SessionDep) -> Response:
    """Delete the direction with the specified id."""
    direction = session.get(Direction, direction_id)
    if not direction:
        raise DirectionNotFoundException()
    session.delete(direction)
    session.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.get(
    '/',
    responses={200: {'description': 'Directions successfully received'}},
    summary='Return a list of directions'
)
def get_directions(session: SessionDep, limit: int = 10, offset: int = 0) -> list[DirectionRead]:
    """Return a list of directions of a given length (limit), starting from a given table entry (offset)."""
    directions = session.execute(select(Direction).offset(offset).limit(limit)).scalars()
    return directions


@router.post(
    '/',
    response_model=DirectionRead,
    status_code=status.HTTP_201_CREATED,
    responses={201: {'description': 'Direction successfully created'}},
    summary='Create the direction'
)
def create_direction(direction_data: DirectionCreate, session: SessionDep) -> Any:
    """Create the direction with the given information."""
    direction = Direction(**direction_data.model_dump())
    session.add(direction)
    session.commit()
    session.refresh(direction)
    return direction
