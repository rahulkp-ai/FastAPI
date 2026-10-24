from pydantic import BaseModel, ConfigDict, Field, EmailStr
from datetime import datetime

class UserBase(BaseModel):
    username: str = Field(min_length=1, max_length=50)
    email:str = Field(max_length=120)

class UserCreate(UserBase):
    pass

class UserResponse(UserBase):
    model_config = ConfigDict(from_attrbute=True)
    
    id:int
    image_file: str | None
    image_path: str

class PostBase(BaseModel):
    title: str = Field(min_length=1, max_length=100)
    content: str = Field(min_length=1)
    

class PostCreate(PostBase):
    user_id: int # temporary

class PostUpdate(BaseModel):
    title: str | None = Field(default = None, min_length=1, max_length=100)
    content: str | None = Field(default = None, min_length=1)

class PostResponse(PostBase):
    model_config = ConfigDict(from_attrbute=True)

    id: int
    user_id: int
    date_posted: datetime
    author: UserResponse



