from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from app.models import MatType
from app.schemas import MatTypeIn, MatTypeUpdate, MatTypeOut

router = APIRouter(prefix="/mat_types", tags=["Материал"])

@router.get("/", response_model=List[MatTypeOut])
def list_mat_types(db: Session = Depends(get_db)):
    return db.query(MatType).order_by(MatType.sort_order, MatType.mat_name).all()

@router.post("/", response_model=MatTypeOut)
def create_mat_type(data: MatTypeIn, db: Session = Depends(get_db)):
    if db.query(MatType).filter(MatType.mat_name == data.mat_name).first():
        raise HTTPException(status_code=400, detail="Материалын нэр давхардсан")
    m = MatType(**data.model_dump())
    db.add(m)
    db.commit()
    db.refresh(m)
    return m

@router.put("/{mat_type_id}", response_model=MatTypeOut)
def update_mat_type(mat_type_id: int, data: MatTypeUpdate, db: Session = Depends(get_db)):
    m = db.query(MatType).filter(MatType.mat_type_id == mat_type_id).first()
    if not m:
        raise HTTPException(status_code=404, detail="Олдсонгүй")
    for k, v in data.model_dump(exclude_unset=True).items():
        setattr(m, k, v)
    db.commit()
    db.refresh(m)
    return m

@router.delete("/{mat_type_id}")
def delete_mat_type(mat_type_id: int, db: Session = Depends(get_db)):
    m = db.query(MatType).filter(MatType.mat_type_id == mat_type_id).first()
    if not m:
        raise HTTPException(status_code=404, detail="Олдсонгүй")
    db.delete(m)
    db.commit()
    return {"detail": "Устгагдлаа"}