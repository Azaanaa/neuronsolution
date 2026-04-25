from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from app.models import SizeType
from app.schemas import SizeTypeIn, SizeTypeUpdate, SizeTypeOut

router = APIRouter(prefix="/size_types", tags=["Размер"])

@router.get("/", response_model=List[SizeTypeOut])
def list_size_types(db: Session = Depends(get_db)):
    return db.query(SizeType).order_by(SizeType.sort_order, SizeType.size_name).all()

@router.post("/", response_model=SizeTypeOut)
def create_size_type(data: SizeTypeIn, db: Session = Depends(get_db)):
    if db.query(SizeType).filter(SizeType.size_name == data.size_name).first():
        raise HTTPException(status_code=400, detail="Размерын нэр давхардсан")
    m = SizeType(**data.model_dump())
    db.add(m)
    db.commit()
    db.refresh(m)
    return m

@router.put("/{size_type_id}", response_model=SizeTypeOut)
def update_size_type(size_type_id: int, data: SizeTypeUpdate, db: Session = Depends(get_db)):
    m = db.query(SizeType).filter(SizeType.size_type_id == size_type_id).first()
    if not m:
        raise HTTPException(status_code=404, detail="Олдсонгүй")
    for k, v in data.model_dump(exclude_unset=True).items():
        setattr(m, k, v)
    db.commit()
    db.refresh(m)
    return m

@router.delete("/{size_type_id}")
def delete_size_type(size_type_id: int, db: Session = Depends(get_db)):
    m = db.query(SizeType).filter(SizeType.size_type_id == size_type_id).first()
    if not m:
        raise HTTPException(status_code=404, detail="Олдсонгүй")
    db.delete(m)
    db.commit()
    return {"detail": "Устгагдлаа"}