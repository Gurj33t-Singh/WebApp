# Database connection setup
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import IntegrityError

DATABASE_URL = "postgresql+psycopg2://admin:04051990@127.0.0.1:5432/localdb"

engine = create_engine(DATABASE_URL)
db_session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
