from pydantic import BaseModel
from typing import Optional
from datetime import date, datetime

class LoginIn(BaseModel):
    user_name: str
    pass_word: str

class UserIn(BaseModel):
    user_name: str
    pass_word: str
    user_role: str

class UserUpdate(BaseModel):
    user_name: Optional[str] = None
    pass_word: Optional[str] = None
    user_role: Optional[str] = None

class UserOut(BaseModel):
    user_id:    int
    user_name:  str
    user_role:  str
    created_at: Optional[datetime] = None
    class Config:
        from_attributes = True

class OrderIn(BaseModel):
    order_id:           str
    order_name:         str
    mat_type:           Optional[str] = None
    model_no:           Optional[str] = None
    custom_model:       Optional[str] = None
    color_code:         Optional[str] = None
    custom_color:       Optional[str] = None
    size_name:          Optional[str] = None
    gage:               Optional[str] = None
    ply:                Optional[str] = None
    order_qnty:         int = 0
    alloc_qnty2:        int = 0
    alloc_qnty3:        int = 0
    alloc_qntyg:        int = 0
    finishDate:         Optional[date] = None
    add_condition:      Optional[str] = None
    order_description:  Optional[str] = None

class OrderUpdate(BaseModel):
    order_id:           Optional[str] = None
    order_name:         Optional[str] = None
    mat_type:           Optional[str] = None
    model_no:           Optional[str] = None
    custom_model:       Optional[str] = None
    color_code:         Optional[str] = None
    custom_color:       Optional[str] = None
    size_name:          Optional[str] = None
    gage:               Optional[str] = None
    ply:                Optional[str] = None
    order_qnty:         int = 0
    alloc_qnty2:        int = 0
    alloc_qnty3:        int = 0
    alloc_qntyg:        int = 0
    finishDate:         Optional[date] = None
    add_condition:      Optional[str] = None
    order_description:  Optional[str] = None

class OrderOut(BaseModel):
    pkey:               int
    order_id:           str
    order_name:         str
    mat_type:           Optional[str] = None
    model_no:           Optional[str] = None
    custom_model:       Optional[str] = None
    color_code:         Optional[str] = None
    custom_color:       Optional[str] = None
    size_name:          Optional[str] = None
    gage:               Optional[str] = None
    ply:                Optional[str] = None
    order_qnty:         int = 0
    alloc_qnty2:        int = 0
    alloc_qnty3:        int = 0
    alloc_qntyg:        int = 0
    finishDate:         Optional[date] = None
    createdAt:          Optional[datetime]
    add_condition:      Optional[str] = None
    order_description:  Optional[str] = None

    class Config:
        from_attributes = True
        
class SettingOut(BaseModel):
    setting_key:   str
    setting_value: str
    class Config:
        from_attributes = True

class SettingUpdate(BaseModel):
    setting_value: str
    
class MatTypeIn(BaseModel):
    mat_name:   str
    sort_order: int = 0

class MatTypeUpdate(BaseModel):
    mat_name:   Optional[str] = None
    sort_order: Optional[int] = None

class MatTypeOut(BaseModel):
    mat_type_id: int
    mat_name:    str
    sort_order:  int
    class Config:
        from_attributes = True
        
class SizeTypeIn(BaseModel):
    size_name:  str
    sort_order: int = 0

class SizeTypeUpdate(BaseModel):
    size_name:  Optional[str] = None
    sort_order: Optional[int] = None

class SizeTypeOut(BaseModel):
    size_type_id: int
    size_name:    str
    sort_order:   int
    class Config:
        from_attributes = True        