
from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    user_name : str
    email_id : EmailStr
    password : str

class UserLogin(BaseModel):
    email_id : EmailStr
    password : str