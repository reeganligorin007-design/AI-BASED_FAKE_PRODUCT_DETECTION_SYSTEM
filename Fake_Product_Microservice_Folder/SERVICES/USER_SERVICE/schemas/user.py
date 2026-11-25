from pydantic import BaseModel,EmailStr
from typing import Optional
from datetime import datetime

class UserCreate(BaseModel):
    
    username : str

    email : EmailStr

    password : str

    role : str = "CUSTOMER"

class UserLogin(BaseModel):

    email: EmailStr

    password : str

   

class UserUpdate(BaseModel):
     
     username: Optional[str] = None

     email : Optional[EmailStr] = None

     role : Optional[str] = None

     is_active : Optional[bool] = None        


class UserResponse(BaseModel):

    id : int

    username : str

    email :EmailStr     

    role : str

    is_active : bool

    created_at : Optional[datetime]

class token(BaseModel):

    access_token : str

    token_type : str