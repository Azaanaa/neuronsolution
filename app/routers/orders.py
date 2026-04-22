from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from app.models import OrderList
from app.schemas import OrderIn, OrderUpdate, OrderOut

router = APIRouter(prefix="/orders", tags=["Захиалга"])

@router.get("/", response_model=List[OrderOut])
def list_orders(db: Session = Depends(get_db)):
    return db.query(OrderList).order_by(OrderList.pkey.desc()).all()

@router.post("/", response_model=OrderOut)
def create_order(data: OrderIn, db: Session = Depends(get_db)):
    order = OrderList(**data.model_dump())
    db.add(order)
    db.commit()
    db.refresh(order)
    return order

@router.put("/{pkey}", response_model=OrderOut)
def update_order(pkey: int, data: OrderUpdate, db: Session = Depends(get_db)):
    order = db.query(OrderList).filter(OrderList.pkey == pkey).first()
    if not order:
        raise HTTPException(status_code=404, detail="Олдсонгүй")
    for k, v in data.model_dump(exclude_unset=True).items():
        setattr(order, k, v)
    db.commit()
    db.refresh(order)
    return order

@router.delete("/{pkey}")
def delete_order(pkey: int, db: Session = Depends(get_db)):
    order = db.query(OrderList).filter(OrderList.pkey == pkey).first()
    if not order:
        raise HTTPException(status_code=404, detail="Олдсонгүй")
    db.delete(order)
    db.commit()
    return {"detail": "Устгагдлаа"}