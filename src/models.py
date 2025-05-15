from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import Integer, String, ForeignKey


class Base(DeclarativeBase):
    pass


class ControlType(Base):
    """Виды контроля дисциплин (зачет, экзамен, дифференцированный зачет)."""
    __tablename__ = 'control_types'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(30), nullable=False, unique=True)


class EducationalLevel(Base):
    """Уровни образования (бакалавриат, магистратура, аспирантура, специалитет)."""
    __tablename__ = 'educational_levels'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(20), nullable=False, unique=True)


class EducationalForm(Base):
    """Формы образования (очная, заочная, очно-заочная)."""
    __tablename__ = 'educational_forms'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(20), nullable=False, unique=True)


class CompetencyGroup(Base):
    """Группы компетенций."""
    __tablename__ = 'competency_groups'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(30), nullable=False, unique=True)

    competencies = relationship('Competency', back_populates='competency_group', cascade='all, delete-orphan')


class Competency(Base):
    """Компетенции."""
    __tablename__ = 'competencies'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    code: Mapped[str] = mapped_column(String(10), nullable=False, unique=True)
    name: Mapped[str] = mapped_column(String(30), nullable=False)
    description: Mapped[str] = mapped_column(String(255), nullable=False)
    competency_group_id: Mapped[int] = mapped_column(Integer, ForeignKey('competency_groups.id'))

    competency_group = relationship('CompetencyGroup', back_populates='competencies')
    indicators = relationship('Indicator', back_populates='competency', cascade='all, delete-orphan')


class Indicator(Base):
    """Индикаторы достижения компетенций."""
    __tablename__ = 'indicators'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    code: Mapped[str] = mapped_column(String(10), nullable=False, unique=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    competency_id: Mapped[int] = mapped_column(Integer, ForeignKey('competencies.id'))

    competency = relationship('Competency', back_populates='indicators')


class DisciplineBlockActivityType(Base):
    """Связи блоков дисциплин и видов учебных занятий."""
    __tablename__ = 'discipline_block_activity_types'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    discipline_block_id: Mapped[int] = mapped_column(Integer, ForeignKey('discipline_blocks.id'))
    activity_type_id: Mapped[int] = mapped_column(Integer, ForeignKey('activity_types.id'))
