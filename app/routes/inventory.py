from fastapi import APIRouter, HTTPException

router = APIRouter()

inventory_db = {
    1: {"id": 1, "name": "Chocolate", "quantity": 0},
}

@router.post("/inventory/{sweet_id}/purchase")
def purchase_sweet(sweet_id: int):
    sweet = inventory_db.get(sweet_id)
    if not sweet:
        raise HTTPException(status_code=404, detail="Sweet not found")
    if sweet["quantity"] <= 0:
        raise HTTPException(status_code=400, detail="Out of stock")
    sweet["quantity"] -= 1
    return {"message": "Purchase successful", "sweet": sweet}

@router.post("/inventory/{sweet_id}/restock")
def restock_sweet(sweet_id: int, quantity: int, admin: bool = True):
    if not admin:
        raise HTTPException(status_code=403, detail="Not authorized")
    sweet = inventory_db.get(sweet_id)
    if not sweet:
        raise HTTPException(status_code=404, detail="Sweet not found")
    sweet["quantity"] += quantity
    return {"message": "Restock successful", "sweet": sweet}
