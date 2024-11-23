# API routes for handling client data

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from core.db import get_db
from core.db_models import Data
from core.schemas import ClientDataCreate, ClientDataResponse

router = APIRouter(prefix="/data", tags=["data"])

@router.post("/create", response_model=ClientDataResponse)
def create_client_data(data: ClientDataCreate, db: Session = Depends(get_db)):
    new_data = Data(**data.dict())
    db.add(new_data)
    db.commit()
    db.refresh(new_data)
    return new_data

@router.post("/search", response_model=ClientDataResponse)
def create_client_data(data: ClientDataCreate, db: Session = Depends(get_db)):
    pass

@router.post("/update", response_model=ClientDataResponse)
def create_client_data(data: ClientDataCreate, db: Session = Depends(get_db)):
    pass
