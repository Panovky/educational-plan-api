from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, ForeignKey


class Base(DeclarativeBase):
    pass


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


class DisciplineBlockActivityType(Base):
    """Связи блоков дисциплин и видов учебных занятий."""
    __tablename__ = 'discipline_block_activity_types'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    discipline_block_id: Mapped[int] = mapped_column(Integer, ForeignKey('discipline_blocks.id'))
    activity_type_id: Mapped[int] = mapped_column(Integer, ForeignKey('activity_types.id'))
