from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
from src import DB_URI
import logging


def start() -> scoped_session:
    try:
        engine = create_engine(DR_URI, client_encoding="utf8")
        BASE.metadata.bind = engine
        BASE.metadata.create_all(engine)
        return scoped_session(sessionmaker(bind=engine, autoflush=False))
    except Exception as sql_error:
        logging.error(
            f"An error occurred while trying to initiate a database connection, {type(sql_error).__name__}: {sql_error}"
        )


BASE = declarative_base()
SESSION = start()

