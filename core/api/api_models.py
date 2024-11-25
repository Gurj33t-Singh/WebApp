from pydantic import BaseModel, Field

class Data(BaseModel):
    phone_number: str = Field(..., description="The phone number of the user")
    field1: str = Field(description="Value for field1")
    field2: str = Field(description="Value for field2")
    field3: str = Field(description="Value for field3")
    field4: str = Field(description="Value for field4")
    field5: str = Field(description="Value for field5")
    field6: str = Field(description="Value for field6")
    field7: str = Field(description="Value for field7")
    field8: str = Field(description="Value for field8")
    field9: str = Field(description="Value for field9")
    field10: bool = Field(description="Value for field10")

    class Config:
        from_attributes = True
