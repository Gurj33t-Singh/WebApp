# Initializes FastAPI app
from fastapi import FastAPI
# Import and include routers
from core.api.data import *

api = FastAPI()


api.include_router(router)
