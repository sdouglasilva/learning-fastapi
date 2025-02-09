from pydantic import BaseModel, EmailStr
from datetime import datetime
from fastapi import FastAPI

from uuid import UUID

class UserIn(BaseModel):
  name:str
  email:EmailStr
  password:str


class UserOut(BaseModel):
  id:UUID
  name:str
  email:str
  fl_active:bool
  created_at: datetime


users = []
app = FastAPI()


@app.post('/users')

def create_user(user:UserIn):
  new_user = user (**user.model_dump())
  users.append(new_user)
  return {'message':' Usuário cadastrado com sucesso;'}


