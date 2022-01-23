from sqlalchemy import create_engine
from src import DB_URL
class SomeTable(Base):
    """
    Class, that represents SomeTable
    """
    __tablename__ = "my_table_in_db"

    __table__ = Table(__tablename__, Base.metadata,
        autoload=True,
        autoload_with=create_engine(DB_URL))

