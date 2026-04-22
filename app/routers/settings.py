from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from app.models import Setting
from app.schemas import SettingOut, SettingUpdate

router = APIRouter(prefix="/settings", tags=["Тохиргоо"])

@router.get("/", response_model=List[SettingOut])
def list_settings(db: Session = Depends(get_db)):
    return db.query(Setting).all()

@router.get("/{key}", response_model=SettingOut)
def get_setting(key: str, db: Session = Depends(get_db)):
    s = db.query(Setting).filter(Setting.setting_key == key).first()
    if not s:
        raise HTTPException(status_code=404, detail="Олдсонгүй")
    return s

@router.put("/{key}", response_model=SettingOut)
def update_setting(key: str, data: SettingUpdate, db: Session = Depends(get_db)):
    s = db.query(Setting).filter(Setting.setting_key == key).first()
    if not s:
        s = Setting(setting_key=key, setting_value=data.setting_value)
        db.add(s)
    else:
        s.setting_value = data.setting_value
    db.commit()
    db.refresh(s)
    return s