from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import models, auth
from ..database import SessionLocal

router = APIRouter(prefix="/api/sweets", tags=["sweets"])

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Get all sweets
@router.get("/")
def get_sweets(db: Session = Depends(get_db)):
    return db.query(models.Sweet).all()

# Add a new sweet (admin only)
@router.post("/")
def add_sweet(name: str, price: float, stock: int, db: Session = Depends(get_db), user=Depends(auth.get_current_admin)):
    sweet = models.Sweet(name=name, price=price, stock=stock)
    db.add(sweet)
    db.commit()
    db.refresh(sweet)
    return sweet

# Update a sweet (admin only)
@router.put("/{sweet_id}")
def update_sweet(sweet_id: int, name: str, price: float, stock: int, db: Session = Depends(get_db), user=Depends(auth.get_current_admin)):
    sweet = db.query(models.Sweet).get(sweet_id)
    if not sweet:
        raise HTTPException(404, "Sweet not found")
    sweet.name, sweet.price, sweet.stock = name, price, stock
    db.commit()
    return sweet

# Delete a sweet (admin only)
@router.delete("/{sweet_id}")
def delete_sweet(sweet_id: int, db: Session = Depends(get_db), user=Depends(auth.get_current_admin)):
    sweet = db.query(models.Sweet).get(sweet_id)
    if not sweet:
        raise HTTPException(404, "Sweet not found")
    db.delete(sweet)
    db.commit()
    return {"message": "Sweet deleted"}

# Purchase sweet (normal user)
@router.post("/{sweet_id}/purchase")
def purchase_sweet(sweet_id: int, quantity: int, db: Session = Depends(get_db), user=Depends(auth.get_current_user)):
    sweet = db.query(models.Sweet).get(sweet_id)
    if not sweet or sweet.stock < quantity:
        raise HTTPException(400, "Not enough stock")
    sweet.stock -= quantity
    db.commit()
    return {"message": f"Purchased {quantity} of {sweet.name}"}

# Restock sweet (admin only)
@router.post("/{sweet_id}/restock")
def restock_sweet(sweet_id: int, quantity: int, db: Session = Depends(get_db), user=Depends(auth.get_current_admin)):
    sweet = db.query(models.Sweet).get(sweet_id)
    if not sweet:
        raise HTTPException(404, "Sweet not found")
    sweet.stock += quantity
    db.commit()
    return {"message": f"Restocked {quantity} of {sweet.name}"}
