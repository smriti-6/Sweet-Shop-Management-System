from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import models, auth

router = APIRouter(prefix="/api/auth", tags=["auth"])

@router.post("/register")
def register(email: str, password: str, db: Session = Depends(auth.get_db)):
    if db.query(models.User).filter_by(email=email).first():
        raise HTTPException(409, "Email exists")
    hashed = auth.hash_password(password)
    user = models.User(email=email, password=hashed, is_admin=False)
    db.add(user)
    db.commit()
    return {"message": "registered"}

@router.post("/login")
def login(email: str, password: str, db: Session = Depends(auth.get_db)):
    user = db.query(models.User).filter_by(email=email).first()
    if not user or not auth.verify_password(password, user.password):
        raise HTTPException(401, "Invalid credentials")
    token = auth.create_access_token({"user_id": user.id, "is_admin": user.is_admin})
    return {"token": token, "user": {"id": user.id, "email": user.email, "is_admin": user.is_admin}}
