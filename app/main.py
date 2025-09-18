from fastapi import FastAPI
from app.routes import sweets

app = FastAPI()

# include router
app.include_router(sweets.router)
