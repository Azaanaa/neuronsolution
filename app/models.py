from sqlalchemy import Column, Integer, String, Date, DateTime, func
from app.database import Base

class User(Base):
    __tablename__ = "users"
    user_id    = Column(Integer, primary_key=True, autoincrement=True)
    user_name  = Column(String(100), nullable=False, unique=True)
    pass_word  = Column(String(255), nullable=False)
    user_role  = Column(String(50), nullable=False)
    created_at = Column(DateTime, default=func.now())

class OrderList(Base):
    __tablename__ = "orderlist"
    pkey                = Column(Integer, primary_key=True, autoincrement=True)
    order_id            = Column(String(50), nullable=False)
    order_name          = Column(String(100), nullable=False)
    mat_type            = Column(String(100))
    model_no            = Column(String(50))
    custom_model        = Column(String(50))
    color_code          = Column(String(50))
    custom_color        = Column(String(50))
    size_name           = Column(String(20))
    gage                = Column(String(20))
    ply                 = Column(String(20))
    order_qnty          = Column(Integer, default=0)
    alloc_qnty2         = Column(Integer, default=0)
    alloc_qnty3         = Column(Integer, default=0)
    alloc_qntyg         = Column(Integer, default=0)
    createdAt           = Column(DateTime, default=func.now())
    finishDate          = Column(Date)
    add_condition       = Column(String(5), default='00000')
    order_description   = Column(String(100))    
    
class Setting(Base):
    __tablename__ = "settings"
    setting_key   = Column(String(50), primary_key=True)
    setting_value = Column(String(255), nullable=False)
    updated_at    = Column(DateTime, default=func.now(), onupdate=func.now())

class MatType(Base):
    __tablename__ = "mat_types"
    mat_type_id = Column(Integer, primary_key=True, autoincrement=True)
    mat_name    = Column(String(100), nullable=False, unique=True)
    sort_order  = Column(Integer, default=0)
    created_at  = Column(DateTime, default=func.now())
    
class SizeType(Base):
    __tablename__ = "size_types"
    size_type_id = Column(Integer, primary_key=True, autoincrement=True)
    size_name    = Column(String(100), nullable=False, unique=True)
    sort_order  = Column(Integer, default=0)
    created_at  = Column(DateTime, default=func.now())    