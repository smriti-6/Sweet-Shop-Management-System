from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse

router = APIRouter(prefix="/api/auth")

users_db = {}  # Temporary in-memory "database"

@router.post("/register")
async def register(email: str, password: str):
    if email in users_db:
        raise HTTPException(status_code=400, detail="User already exists")
    users_db[email] = password
    return JSONResponse(content={"msg": "User registered successfully"})

@router.post("/login")
async def login(email: str, password: str):
    if users_db.get(email) != password:
        raise HTTPException(status_code=400, detail="Invalid credentials")
    return JSONResponse(content={"token": "dummy-token"})
