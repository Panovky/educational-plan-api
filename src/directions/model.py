from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from src.core.base_model import Base


class Direction(Base):
    """Направления подготовки."""
    __tablename__ = 'directions'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    educational_level_id: Mapped[int] = mapped_column(Integer, ForeignKey('educational_levels.id'))
    educational_form_id: Mapped[int] = mapped_column(Integer, ForeignKey('educational_forms.id'))
    semester_count: Mapped[int] = mapped_column(Integer, nullable=False)
