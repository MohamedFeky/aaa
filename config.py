import psycopg2
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy_utils import database_exists, create_database

engine = create_engine("postgresql://postgres:132000@localhost:5432/libraryManagement", echo=True)
if not database_exists(engine.url):
    create_database(engine.url)

Base = declarative_base()
print(database_exists(engine.url))                 