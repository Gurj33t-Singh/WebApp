# Pydantic schemas for request/response validation
from pydantic import BaseModel

class ClientDataCreate(BaseModel):
    field1: str
    field2: str
    # Add other fields

class ClientDataResponse(BaseModel):
    id: int
    field1: str
    field2: str
    # Add other fields

    class Config:
        orm_mode = True
