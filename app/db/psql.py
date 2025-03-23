from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from dotenv import load_dotenv
import os

load_dotenv(verbose=True)
engine = create_engine(os.getenv("DATABASE_URL"))

psql_session = sessionmaker(bind=engine)

Base = declarative_base()
