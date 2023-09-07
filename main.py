from fastapi import FastAPI
import models
from database import engine
from routers import auth, admin, users, houses, squares, cities, house_features
from cors_middleware import cors_middleware  # Assicurati che il percorso sia corretto



app = FastAPI()

models.Base.metadata.create_all(bind=engine)


app.add_middleware(cors_middleware)
app.include_router(admin.router)
app.include_router(users.router)
app.include_router(auth.router)
app.include_router(houses.router)
app.include_router(house_features.router)
app.include_router(squares.router)
app.include_router(cities.router)


#Start server uvicorn
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host='localhost', port=8000)
