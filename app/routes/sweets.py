from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import models, schemas
from app.database import get_db

router = APIRouter(
    prefix="/sweets",
    tags=["sweets"]
)

# Create Sweet
@router.post("/", response_model=schemas.SweetResponse)
def create_sweet(sweet: schemas.SweetCreate, db: Session = Depends(get_db)):
    db_sweet = models.Sweet(**sweet.dict())
    db.add(db_sweet)
    db.commit()
    db.refresh(db_sweet)
    return db_sweet


# Get all Sweets
@router.get("/", response_model=list[schemas.SweetResponse])
def get_sweets(db: Session = Depends(get_db)):
    sweets = db.query(models.Sweet).all()
    return sweets


# Get Sweet by ID
@router.get("/{sweet_id}", response_model=schemas.SweetResponse)
def get_sweet(sweet_id: int, db: Session = Depends(get_db)):
    sweet = db.query(models.Sweet).filter(models.Sweet.id == sweet_id).first()
    if not sweet:
        raise HTTPException(status_code=404, detail="Sweet not found")
    return sweet


# Update Sweet
@router.put("/{sweet_id}", response_model=schemas.SweetResponse)
def update_sweet(sweet_id: int, sweet: schemas.SweetCreate, db: Session = Depends(get_db)):
    db_sweet = db.query(models.Sweet).filter(models.Sweet.id == sweet_id).first()
    if not db_sweet:
        raise HTTPException(status_code=404, detail="Sweet not found")

    for key, value in sweet.dict().items():
        setattr(db_sweet, key, value)

    db.commit()
    db.refresh(db_sweet)
    return db_sweet


# Delete Sweet
@router.delete("/{sweet_id}")
def delete_sweet(sweet_id: int, db: Session = Depends(get_db)):
    db_sweet = db.query(models.Sweet).filter(models.Sweet.id == sweet_id).first()
    if not db_sweet:
        raise HTTPException(status_code=404, detail="Sweet not found")

    db.delete(db_sweet)
    db.commit()
    return {"message": "Sweet deleted successfully"}
