# API routes for handling client data
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import desc

from core.db.db_core import get_db
from core.db import db_models
from core.api import api_models

router = APIRouter(prefix="/data", tags=["data"])

@router.post("/create", response_model=api_models.Data)
def create_data(data: api_models.Data, db: Session = Depends(get_db)):
    new_data = db_models.Data(**data.__dict__)
    db.add(new_data)
    db.commit()
    db.refresh(new_data)
    return new_data

@router.post("/search", response_model=list[api_models.Data])
def search_data(
    phone_number: str = None, 
    size: int = 10, 
    db: Session = Depends(get_db)
):
    # If phone_number is provided, search by phone_number
    if phone_number:
        data = db.query(db_models.Data).filter(db_models.Data.phone_number == phone_number).order_by(desc(db_models.Data.created_time)).all()
    else:
        # If no phone_number is provided, return all data with pagination based on `size`, ordered by created_time in descending order
        data = db.query(db_models.Data).order_by(desc(db_models.Data.created_time)).limit(size).all()

    # If no data is found, raise a 404 HTTPException
    if not data:
        raise HTTPException(status_code=404, detail="No data found")

    # Return the data
    return data

@router.post("/update", response_model=api_models.Data)
def update_data(phone_number: str, data: api_models.Data, db: Session = Depends(get_db)):
    # Find the existing record by primary key (phone_number)
    db_data = db.query(db_models.Data).filter(db_models.Data.phone_number == phone_number).first()

    if not db_data:
        raise HTTPException(status_code=404, detail="Data not found")
    
    # Update fields only if provided in the payload
    for field, value in data.model_dump(exclude_unset=True).items():  # exclude_unset ensures only provided fields are updated
        setattr(db_data, field, value)

    # Commit changes to the database
    db.commit()
    db.refresh(db_data)
    
    return db_data

@router.post("/delete", response_model=str)
def delete_data(phone_number: str, db: Session = Depends(get_db)):
    # Find the record by phone number
    db_data = db.query(db_models.Data).filter(db_models.Data.phone_number == phone_number).first()
    
    if not db_data:
        raise HTTPException(status_code=404, detail="Data not found")
    
    # Delete the record
    db.delete(db_data)
    db.commit()

    # Return a custom success message
    return f"The record with Phone No. {phone_number} has been deleted successfully"