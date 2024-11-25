# Database connection setup
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from core import utils

db = utils.read_json("config.json")["db"]

DATABASE_URL = f"postgresql+psycopg2://{db['username']}:{db['password']}@{db['host_ip']}:{db['port']}/{db['db_name']}"

engine = create_engine(DATABASE_URL)
db_session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
