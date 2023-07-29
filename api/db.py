import sqlalchemy
import databases
import aiosqlite
from databases import Database
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from sqlalchemy import (
    Column,
    Integer,
    MetaData,
    String,
    Table,
    create_engine
)


# DATABASE_URL = "mysql://root:@localhost/articledb"
# engine = create_engine(DATABASE_URL)

metadata = sqlalchemy.MetaData()
database = databases.Database("sqlite:///sqlite.db")
engine = sqlalchemy.create_engine("sqlite:///sqlite.db")

sessionlocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


Article = Table(

    'article',
    metadata,
    Column("id", Integer, primary_key=True),
    Column("title", String(100)),
    Column("description", String(500))

)
# class Article(Base):
#     __tablename__ = 'articledb'
#
#     Column("id", Integer, primary_key=True)
#     Column("title", String(100))
#     Column("description", String(500))
#
# Base.metadata.create_all(bind=engine)

