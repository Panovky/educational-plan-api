from sqlalchemy.orm import Session
from src.core.sqlalchemy_repository import SQLAlchemyRepository
from src.indicators.model import Indicator
from src.competency_groups.model import CompetencyGroup
from src.activity_types.model import ActivityType


class ActivityTypesRepository(SQLAlchemyRepository):
    def __init__(self, session: Session):
        super().__init__(session, ActivityType)


class CompetencyGroupsRepository(SQLAlchemyRepository):
    def __init__(self, session: Session):
        super().__init__(session, CompetencyGroup)


class IndicatorsRepository(SQLAlchemyRepository):
    def __init__(self, session: Session):
        super().__init__(session, Indicator)
