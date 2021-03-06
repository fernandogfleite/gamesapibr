from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
import databases
from decouple import config

DATABASE_URL = config("DB_URL")

database = databases.Database(DATABASE_URL)

engine = create_engine(
    DATABASE_URL
)

Base = declarative_base()
