from pydantic import BaseModel
from enum import Enum


class Gender(str,Enum):
  MALE = 'M'
  FEMALE = 'F'
  OTHER = 'O'

class Person(BaseModel):
  name: str
  age: int
  heigth:float
