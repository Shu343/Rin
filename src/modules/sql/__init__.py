from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
from src import DB_URI

class SomeTable(Base):
    """
    Class, that represents SomeTable
    """
    __tablename__ = "my_table_in_db"

    __table__ = Table(__tablename__, Base.metadata,
        autoload=True,
        autoload_with=create_engine(DB_URL))


def start() -> scoped_session:
    engine = create_engine(DB_URI, client_encoding="utf8")
    BASE.metadata.bind = engine
    BASE.metadata.create_all(engine)
    return scoped_session(sessionmaker(bind=engine, autoflush=False))


BASE = declarative_base()
SESSION = start()

