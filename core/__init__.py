# Initializes FastAPI app

from fastapi import FastAPI

api = FastAPI()

# Import and include routers
from core.routes import data
api.include_router(data.router)
