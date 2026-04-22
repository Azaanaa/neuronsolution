from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from app.models import User
from app.schemas import UserIn, UserUpdate, UserOut

router = APIRouter(prefix="/users", tags=["Хэрэглэгч"])

@router.get("/", response_model=List[UserOut])
def list_users(db: Session = Depends(get_db)):
    return db.query(User).order_by(User.user_id).all()

@router.post("/", response_model=UserOut)
def create_user(data: UserIn, db: Session = Depends(get_db)):
    if db.query(User).filter(User.user_name == data.user_name).first():
        raise HTTPException(status_code=400, detail="Хэрэглэгчийн нэр давхардсан")
    user = User(**data.model_dump())
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

@router.put("/{user_id}", response_model=UserOut)
def update_user(user_id: int, data: UserUpdate, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.user_id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="Олдсонгүй")
    for k, v in data.model_dump(exclude_unset=True).items():
        setattr(user, k, v)
    db.commit()
    db.refresh(user)
    return user

@router.delete("/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.user_id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="Олдсонгүй")
    db.delete(user)
    db.commit()
    return {"detail": "Устгагдлаа"}