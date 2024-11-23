# SQLAlchemy database models
from sqlalchemy import Column, Integer, String, Text, func
from sqlalchemy.dialects.postgresql import UUID

from core.db import Base

class Data(Base):
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
    field10 = Column(Text)