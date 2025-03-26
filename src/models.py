from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import Integer, String, Boolean, ForeignKey


class Base(DeclarativeBase):
    pass


class Discipline(Base):
    """Информация о дисциплинах."""
    __tablename__ = 'disciplines'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False, unique=True)


class AssessmentType(Base):
    """Виды аттестации (зачеты, экзамены и т.д.)."""
    __tablename__ = 'assessment_types'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(11), nullable=False, unique=True)


class Department(Base):
    """Информация о кафедрах."""
    __tablename__ = 'departments'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False, unique=True)


class DisciplineBlock(Base):
    """Блоки дисциплин и их характеристики."""
    __tablename__ = 'discipline_blocks'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    discipline_id: Mapped[int] = mapped_column(Integer, ForeignKey('disciplines.id'))
    educational_type_id: Mapped[int] = mapped_column(Integer, ForeignKey('educational_types.id'))
    semester_number: Mapped[int] = mapped_column(Integer, nullable=False)
    credit_units: Mapped[int] = mapped_column(Integer, nullable=False)
    assessment_type_id: Mapped[int] = mapped_column(Integer, ForeignKey('assessment_types.id'))
    has_coursework: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_project: Mapped[bool] = mapped_column(Boolean, nullable=False)
    department_id: Mapped[int] = mapped_column(Integer, ForeignKey('departments.id'))
    lecture_hours: Mapped[int] = mapped_column(Integer, nullable=False)
    practice_hours: Mapped[int] = mapped_column(Integer, nullable=False)
    lab_hours: Mapped[int] = mapped_column(Integer, nullable=False)


class Competency(Base):
    """Компетенции."""
    __tablename__ = 'competencies'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(20), nullable=False)


class CompetencyIndicator(Base):
    """Индикаторы компетенций."""
    __tablename__ = 'competency_indicators'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    competency_code_id: Mapped[int] = mapped_column(Integer, ForeignKey('competency_codes.id'))
    name: Mapped[str] = mapped_column(String(100), nullable=False, unique=True)


class DisciplineBlockCompetency(Base):
    """Связь блоков дисциплин и компетенций."""
    __tablename__ = 'discipline_block_competencies'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    competency_code_id: Mapped[int] = mapped_column(Integer, ForeignKey('competency_codes.id'))
    discipline_block_id: Mapped[int] = mapped_column(Integer, ForeignKey('discipline_blocks.id'))


class CompetencyCode(Base):
    """Коды компетенций."""
    __tablename__ = 'competency_codes'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(5), nullable=False)
    additional_competency_id: Mapped[int] = mapped_column(Integer, ForeignKey('competencies.id'))


class EducationalType(Base):
    """Бакалавриат, магистратура и т.д."""
    __tablename__ = 'educational_types'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(20), nullable=False, unique=True)
    semester_count: Mapped[int] = mapped_column(Integer, nullable=False)



