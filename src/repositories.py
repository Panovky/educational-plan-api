from abc import ABC, abstractmethod
from sqlalchemy import select, func
from sqlalchemy.orm import Session
from typing import TypeVar, Generic
from src.models import (
    ActivityType, Competency, CompetencyGroup, ControlType, Department, Direction, DisciplineBlock, Discipline,
    Indicator
)

T = TypeVar('T')


class AbstractRepository(ABC, Generic[T]):
    @abstractmethod
    def get_all(self) -> list[T]:
        raise NotImplementedError

    @abstractmethod
    def get_by_id(self, _id: int) -> T | None:
        raise NotImplementedError

    @abstractmethod
    def create(self, data: dict) -> T:
        raise NotImplementedError

    @abstractmethod
    def update(self, _id: int, data: dict) -> T | None:
        raise NotImplementedError

    @abstractmethod
    def delete(self, _id: int) -> bool:
        raise NotImplementedError

    @abstractmethod
    def filter_by(self, **filters) -> list[T]:
        raise NotImplementedError

    @abstractmethod
    def starts_with(self, atr_name: str, prefix: str, case_sensitive: bool = False) -> list[T]:
        raise NotImplementedError

    @abstractmethod
    def exists(self, **filters) -> bool:
        raise NotImplementedError


class SQLAlchemyRepository(AbstractRepository, Generic[T]):
    def __init__(self, session: Session, model: T):
        self.session: Session = session
        self.model: T = model

    def get_all(self) -> list[T]:
        stmt = select(self.model)
        res = self.session.execute(stmt)
        return list(res.scalars())

    def get_by_id(self, _id: int) -> T | None:
        res = self.session.get(self.model, _id)
        return res

    def create(self, data: dict) -> T:
        instance = self.model(**data)
        self.session.add(instance)
        self.session.commit()
        self.session.refresh(instance)
        return instance

    def update(self, _id: int, data: dict) -> T | None:
        instance = self.get_by_id(_id)
        if not instance:
            return None

        for key, value in data.items():
            setattr(instance, key, value)

        self.session.commit()
        self.session.refresh(instance)
        return instance

    def delete(self, _id: int) -> bool:
        instance = self.get_by_id(_id)
        if not instance:
            return False

        self.session.delete(instance)
        self.session.commit()
        return True

    def filter_by(self, **filters) -> list[T]:
        stmt = select(self.model).filter_by(**filters)
        res = self.session.execute(stmt)
        return list(res.scalars())

    def starts_with(self, atr_name: str, prefix: str, case_sensitive: bool = False) -> list[T]:
        atr = getattr(self.model, atr_name)
        stmt = select(self.model)

        if case_sensitive:
            stmt = stmt.where(atr.startswith(prefix))
        else:
            stmt = stmt.where(func.lower(atr).startswith(prefix.lower()))

        res = self.session.execute(stmt)
        return list(res.scalars())

    def exists(self, **filters) -> bool:
        stmt = select(self.model).filter_by(**filters)
        res = self.session.exists(stmt)
        return res.scalar()


class ActivityTypesRepository(SQLAlchemyRepository):
    def __init__(self, session: Session):
        super().__init__(session, ActivityType)


class CompetenciesRepository(SQLAlchemyRepository):
    def __init__(self, session: Session):
        super().__init__(session, Competency)


class CompetencyGroupsRepository(SQLAlchemyRepository):
    def __init__(self, session: Session):
        super().__init__(session, CompetencyGroup)


class ControlTypesRepository(SQLAlchemyRepository):
    def __init__(self, session: Session):
        super().__init__(session, ControlType)


class DepartmentsRepository(SQLAlchemyRepository):
    def __init__(self, session: Session):
        super().__init__(session, Department)


class DirectionsRepository(SQLAlchemyRepository):
    def __init__(self, session: Session):
        super().__init__(session, Direction)


class DisciplineBlocksRepository(SQLAlchemyRepository):
    def __init__(self, session: Session):
        super().__init__(session, DisciplineBlock)


class DisciplinesRepository(SQLAlchemyRepository):
    def __init__(self, session: Session):
        super().__init__(session, Discipline)


class IndicatorsRepository(SQLAlchemyRepository):
    def __init__(self, session: Session):
        super().__init__(session, Indicator)
