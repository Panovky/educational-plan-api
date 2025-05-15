from sqlalchemy.orm import Session
from src.core.sqlalchemy_repository import SQLAlchemyRepository
from src.models import ActivityType, Competency, CompetencyGroup, ControlType, Indicator
from src.departments.model import Department
from src.disciplines.model import Discipline


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


class DisciplinesRepository(SQLAlchemyRepository):
    def __init__(self, session: Session):
        super().__init__(session, Discipline)


class IndicatorsRepository(SQLAlchemyRepository):
    def __init__(self, session: Session):
        super().__init__(session, Indicator)
