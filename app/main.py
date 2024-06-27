from fastapi import FastAPI
from app.routes import api_router


app = FastAPI(title="WorkoutApi")
app.include_router(api_router)
