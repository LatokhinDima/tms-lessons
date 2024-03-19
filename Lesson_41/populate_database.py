import os

from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database

DB_PATH = os.path.abspath('db.sqlite3')
engine = create_engine(f'sqlite:////{DB_PATH}', echo=True)
if not database_exists(engine.url):
    create_database(engine.url)
