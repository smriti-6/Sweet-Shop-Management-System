from fastapi import FastAPI
from .routes import auth, sweets
from .database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(auth.router)
app.include_router(sweets.router)

@app.get("/")
def root():
    return {"msg": "Sweet Shop API running"}
