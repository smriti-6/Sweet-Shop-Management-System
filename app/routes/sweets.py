from fastapi import APIRouter, HTTPException

router = APIRouter()

# In-memory database (temporary for TDD)
sweets_db = []
counter = 1  # for unique IDs


# Add sweet
@router.post("/sweets")
def add_sweet(name: str, category: str, price: int, quantity: int):
    global counter
    sweet = {
        "id": counter,
        "name": name,
        "category": category,
        "price": price,
        "quantity": quantity,
    }
    sweets_db.append(sweet)
    counter += 1
    return sweet


# Get all sweets
@router.get("/sweets")
def get_sweets():
    return sweets_db


# Update sweet
@router.put("/sweets/{sweet_id}")
def update_sweet(sweet_id: int, name: str = None, category: str = None, price: int = None, quantity: int = None):
    for sweet in sweets_db:
        if sweet["id"] == sweet_id:
            if name:
                sweet["name"] = name
            if category:
                sweet["category"] = category
            if price:
                sweet["price"] = price
            if quantity:
                sweet["quantity"] = quantity
            return sweet
    raise HTTPException(status_code=404, detail="Sweet not found")


# Delete sweet
@router.delete("/sweets/{sweet_id}")
def delete_sweet(sweet_id: int):
    for sweet in sweets_db:
        if sweet["id"] == sweet_id:
            sweets_db.remove(sweet)
            return {"message": "Sweet deleted"}
    raise HTTPException(status_code=404, detail="Sweet not found")


# Search sweets
@router.get("/sweets/search")
def search_sweets(name: str):
    results = [sweet for sweet in sweets_db if name.lower() in sweet["name"].lower()]
    return results
