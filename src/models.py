from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, ForeignKey


class Base(DeclarativeBase):
    pass


class Discipline(Base):
    """Дисциплины."""
    __tablename__ = 'disciplines'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False, unique=True)
    short_name: Mapped[str] = mapped_column(String(50), nullable=False, unique=True)


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
    name: Mapped[str] = mapped_column(String(20), nullable=False)
    direction_id: Mapped[int] = mapped_column(Integer, ForeignKey('directions.id'))


class Competency(Base):
    """Компетенции."""
    __tablename__ = 'competencies'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(20), nullable=False)


class CompetencyCode(Base):
    """Коды компетенций."""
    __tablename__ = 'competency_codes'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(5), nullable=False)
    competency_id: Mapped[int] = mapped_column(Integer, ForeignKey('competencies.id'))


class Indicator(Base):
    """Индикаторы."""
    __tablename__ = 'indicators'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False, unique=True)
    competency_code_id: Mapped[int] = mapped_column(Integer, ForeignKey('competency_codes.id'))


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
    department_id: Mapped[int] = mapped_column(Integer, ForeignKey('departments.id'))
    lecture_hours: Mapped[int] = mapped_column(Integer, nullable=False)
    practice_hours: Mapped[int] = mapped_column(Integer, nullable=False)
    lab_hours: Mapped[int] = mapped_column(Integer, nullable=False)
    semester_number: Mapped[int] = mapped_column(Integer, nullable=False)
    map_core_id: Mapped[int] = mapped_column(Integer, ForeignKey('map_cors.id'))
    direction_id: Mapped[int] = mapped_column(Integer, ForeignKey('directions.id'))


class DisciplineBlockCompetencyCode(Base):
    """Связи блоков дисциплин и кодов компетенций."""
    __tablename__ = 'discipline_block_competency_codes'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    discipline_block_id: Mapped[int] = mapped_column(Integer, ForeignKey('discipline_blocks.id'))
    competency_code_id: Mapped[int] = mapped_column(Integer, ForeignKey('competency_codes.id'))
