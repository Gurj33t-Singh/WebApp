# SQLAlchemy database models
from sqlalchemy import Column, String, Text, func, DateTime, Boolean
from sqlalchemy.dialects.postgresql import UUID

from core.db import db_conn

class Data(db_conn.Base):
    __tablename__ = 'data'

    uuid_field = Column(UUID(as_uuid=True), default=func.gen_random_uuid(), primary_key=True)  # UUID field with auto-generated value
    phone_number = Column(String(15), primary_key=True)  # Field for phone number as the primary key
    field1 = Column(Text)
    field2 = Column(Text)
    field3 = Column(Text)
    field4 = Column(Text)
    field5 = Column(Text)
    field6 = Column(Text)
    field7 = Column(Text)
    field8 = Column(Text)
    field9 = Column(Text)
    field10 = Column(Boolean)
    # Adding created and updated time
    created_time = Column(DateTime, default=func.now())
    updated_time = Column(DateTime, default=func.now(), onupdate=func.now())  # Will update automatically on record change