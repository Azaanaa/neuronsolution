from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.database import engine
from app import models
from app.routers import auth, users, orders, settings, mat_types, size_types

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Neuron Solution WIP")

app.include_router(auth.router)
app.include_router(users.router)
app.include_router(orders.router)
app.include_router(settings.router)
app.include_router(mat_types.router)
app.include_router(size_types.router)

app.mount("/", StaticFiles(directory="app/static", html=True), name="static")