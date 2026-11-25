from sqlalchemy import Column,String,Boolean,Integer,TIMESTAMP
from sqlalchemy.sql import func
from core.database import base

class User(base):
    __tablename__="users"
    id = Column(Integer,primary_key=True,index=True)
    username =Column(String(100),nullable =False)
    email = Column(String(150),unique=True,nullable=False,index=True)
    password_hash = Column(String(255),nullable=False)
    role = Column(String(20),default="CUSTOMER")
    is_active = Column(Boolean,default=True)
    created_at = Column(TIMESTAMP,server_default = func.current_timestamp())