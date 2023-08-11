from datetime import date
from sqlalchemy.orm import Session

from src.models import Base, Birthday
from src.engine import engine


if __name__ == "__main__":
    Base.metadata.create_all(engine)
    with Session(engine) as session:
        bday_1 = Birthday(
            day=date(2015, 12, 23),
        )
        session.add(bday_1)
        session.commit()
