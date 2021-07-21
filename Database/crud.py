from contextlib import contextmanager

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from Database.models import Base


engine = create_engine("sqlite:///cow.db")
Session = sessionmaker(bind=engine)


@contextmanager
def session_scope():
    """
    create the context manager for connecting to the db session
    """
    session = Session()
    try:
        yield session
        session.commit()
    except Exception:
        session.rollback()
    finally:
        session.close()


def create_database(engine=engine):
    """
    create the database as specified in models.py
    """
    Base.metadata.create_all(engine)


if __name__ == "__main__":
    create_database()
