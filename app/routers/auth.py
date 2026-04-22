from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import User
from app.schemas import LoginIn

router = APIRouter(prefix="/auth", tags=["Нэвтрэх"])

@router.post("/login")
def login(data: LoginIn, db: Session = Depends(get_db)):
    user = db.query(User).filter(
        User.user_name == data.user_name,
        User.pass_word == data.pass_word
    ).first()
    if not user:
        raise HTTPException(status_code=401, detail="Нэвтрэх нэр эсвэл нууц үг буруу")
    return {
        "user_id":   user.user_id,
        "user_name": user.user_name,
        "user_role": user.user_role
    }