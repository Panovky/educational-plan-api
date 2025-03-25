from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import Integer, String, Boolean, ForeignKey


class Base(DeclarativeBase):
    pass


class Discipline(Base):
    """Информация о дисциплинах."""
    __tablename__ = 'disciplines'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False, unique=True)

    discipline_blocks = relationship('DisciplineBlock', back_populates='discipline')


class AssessmentType(Base):
    """Виды аттестации (зачеты, экзамены и т.д.)."""
    __tablename__ = 'assessment_types'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(11), nullable=False, unique=True)

    discipline_blocks = relationship('DisciplineBlock', back_populates='assessment_type')


class Department(Base):
    """Информация о кафедрах."""
    __tablename__ = 'departments'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False, unique=True)

    discipline_blocks = relationship('DisciplineBlock', back_populates='department')


class DisciplineBlock(Base):
    """Блоки дисциплин и их характеристики."""
    __tablename__ = 'discipline_blocks'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    discipline_id: Mapped[int] = mapped_column(Integer, ForeignKey('disciplines.id'))
    credit_units: Mapped[int] = mapped_column(Integer, nullable=False)
    assessment_type_id: Mapped[int] = mapped_column(Integer, ForeignKey('assessment_types.id'))
    has_coursework: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_project: Mapped[bool] = mapped_column(Boolean, nullable=False)
    department_id: Mapped[int] = mapped_column(Integer, ForeignKey('departments.id'))
    lecture_hours: Mapped[int] = mapped_column(Integer, nullable=False)
    practice_hours: Mapped[int] = mapped_column(Integer, nullable=False)
    lab_hours: Mapped[int] = mapped_column(Integer, nullable=False)

    discipline = relationship('Discipline', back_populates='discipline_blocks')
    assessment_type = relationship('AssessmentType', back_populates='discipline_blocks')
    department = relationship('Department', back_populates='discipline_blocks')


class Competency(Base):
    """Компетенции."""
    __tablename__ = 'competencies'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(20), nullable=False)

    competency_codes = relationship('CompetencyCode', back_populates='competency')


class CompetencyIndicator(Base):
    """Индикаторы компетенций."""
    __tablename__ = 'competency_indicators'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    competency_code_id: Mapped[int] = mapped_column(Integer, ForeignKey('competency_codes.id'))
    name: Mapped[str] = mapped_column(String(100), nullable=False, unique=True)

    competency_code = relationship('CompetencyCode', back_populates='competency_indicators')


class DisciplineBlockCompetency(Base):
    """Связь блоков дисциплин и компетенций."""
    __tablename__ = 'discipline_block_competencies'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    competency_code_id: Mapped[int] = mapped_column(Integer, ForeignKey('competency_codes.id'))
    discipline_block_id: Mapped[int] = mapped_column(Integer, ForeignKey('discipline_blocks.id'))

    competency_code = relationship('CompetencyCode', back_populates='discipline_block_competencies')
    discipline_block = relationship('Discipline', back_populates='discipline_block_competencies')


class CompetencyCode(Base):
    """Коды компетенций."""
    __tablename__ = 'competency_codes'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(5), nullable=False)
    additional_competency_id: Mapped[int] = mapped_column(Integer, ForeignKey('competencies.id'))

    competency = relationship('Competency', back_populates='competency_codes')
