from fastapi import FastAPI
from app.routes.users_routes import users_router
from app.routes.visual_routes import visual_router
from app.routes.food_item_routes import food_item_router
from fastapi.middleware.cors import CORSMiddleware
from app.models import *
from app.db.psql import Base, engine

app = FastAPI(title="nutrition_app")

app.include_router(users_router)
app.include_router(visual_router)
app.include_router(food_item_router)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Your React app's origin
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods including OPTIONS for preflight
    allow_headers=["*"],  # Allow all headers
)

Base.metadata.create_all(bind=engine)
