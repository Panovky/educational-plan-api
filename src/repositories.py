from sqlalchemy.orm import Session
from src.core.sqlalchemy_repository import SQLAlchemyRepository
from src.indicators.model import Indicator
from src.control_types.model import ControlType
from src.competency_groups.model import CompetencyGroup
from src.competencies.model import Competency
from src.activity_types.model import ActivityType


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


class IndicatorsRepository(SQLAlchemyRepository):
    def __init__(self, session: Session):
        super().__init__(session, Indicator)
