from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import Integer, String, ForeignKey


class Base(DeclarativeBase):
    pass


class ControlType(Base):
    """Виды контроля дисциплин (зачет, экзамен, дифференцированный зачет)."""
    __tablename__ = 'control_types'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(30), nullable=False, unique=True)


class Department(Base):
    """Кафедры."""
    __tablename__ = 'departments'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False, unique=True)
    disciplines = relationship('Discipline', back_populates='department', cascade='all, delete-orphan')


class Discipline(Base):
    """Дисциплины."""
    __tablename__ = 'disciplines'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False, unique=True)
    short_name: Mapped[str] = mapped_column(String(50), nullable=False, unique=True)
    department_id: Mapped[int] = mapped_column(Integer, ForeignKey('departments.id'))

    department = relationship('Department', back_populates='disciplines')


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


class Direction(Base):
    """Направления подготовки."""
    __tablename__ = 'directions'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False, unique=True)
    educational_level_id: Mapped[int] = mapped_column(Integer, ForeignKey('educational_levels.id'))
    educational_form_id: Mapped[int] = mapped_column(Integer, ForeignKey('educational_forms.id'))
    semester_count: Mapped[int] = mapped_column(Integer, nullable=False)


class MapCore(Base):
    """Ядра карты."""
    __tablename__ = 'map_cors'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False)


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
    name: Mapped[str] = mapped_column(String(255), nullable=False)
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


class ActivityType(Base):
    """Виды учебных занятий (практические занятия, лекции, лабораторные работы)."""
    __tablename__ = 'activity_types'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(30), nullable=False, unique=True)


class DisciplineBlockActivityType(Base):
    """Связи блоков дисциплин и видов учебных занятий."""
    __tablename__ = 'discipline_block_activity_types'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    discipline_block_id: Mapped[int] = mapped_column(Integer, ForeignKey('discipline_blocks.id'))
    activity_type_id: Mapped[int] = mapped_column(Integer, ForeignKey('activity_types.id'))


class DisciplineBlock(Base):
    """Блоки дисциплин."""
    __tablename__ = 'discipline_blocks'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    discipline_id: Mapped[int] = mapped_column(Integer, ForeignKey('disciplines.id'))
    credit_units: Mapped[int] = mapped_column(Integer, nullable=False)
    control_type_id: Mapped[int] = mapped_column(Integer, ForeignKey('control_types.id'))
    lecture_hours: Mapped[int] = mapped_column(Integer, nullable=False)
    practice_hours: Mapped[int] = mapped_column(Integer, nullable=False)
    lab_hours: Mapped[int] = mapped_column(Integer, nullable=False)
    semester_number: Mapped[int] = mapped_column(Integer, nullable=False)
    map_core_id: Mapped[int] = mapped_column(Integer, ForeignKey('map_cors.id'))


class DisciplineBlockCompetency(Base):
    """Связи блоков дисциплин и компетенций."""
    __tablename__ = 'discipline_block_competencies'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    discipline_block_id: Mapped[int] = mapped_column(Integer, ForeignKey('discipline_blocks.id'))
    competency_id: Mapped[int] = mapped_column(Integer, ForeignKey('competencies.id'))


class DirectionMapCore(Base):
    """Связи направлений подготовки и ядер карт."""
    __tablename__ = 'direction_map_cors'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    direction_id: Mapped[int] = mapped_column(Integer, ForeignKey('directions.id'))
    map_core_id: Mapped[int] = mapped_column(Integer, ForeignKey('map_cors.id'))