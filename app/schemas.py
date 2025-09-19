from pydantic import BaseModel

class SweetBase(BaseModel):
    name: str
    category: str
    price: float
    quantity: int

class SweetCreate(SweetBase):
    pass

class SweetResponse(SweetBase):
    id: int

    class Config:
        orm_mode = True
