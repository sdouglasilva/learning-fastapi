from pydantic import BaseModel, EmailStr
from models import Gender


class PersonIn(BaseModel):
  name: str
  age: int
  heigth: float
  gender: Gender

class PersonOut(BaseModel):
  name: str
  email: EmailStr
  age: int
  heigth: float
  gender: Gender

class MessageOut(BaseModel):
  message:str
