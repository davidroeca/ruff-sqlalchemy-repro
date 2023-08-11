"""The failing example."""
from __future__ import annotations

from datetime import date

from sqlalchemy.orm import Mapped, mapped_column

from .base import Base

class Birthday(Base):
    """Silly table to reproduce issue."""

    __tablename__ = "birthday"
    id: Mapped[int] = mapped_column(primary_key=True)  # noqa: A003
    day: Mapped[date]
