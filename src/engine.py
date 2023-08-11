"""Define the base engine for SQLAlchemy."""
from sqlalchemy import create_engine

engine = create_engine("sqlite://", echo=True)
