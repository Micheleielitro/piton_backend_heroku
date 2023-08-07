from fastapi import FastAPI
import models
from database import engine
from routers import auth, admin, users, houses, squares, cities, house_features

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

app.include_router(auth.router)
app.include_router(houses.router)
app.include_router(house_features.router)
app.include_router(squares.router)
app.include_router(cities.router)
app.include_router(admin.router)
app.include_router(users.router)