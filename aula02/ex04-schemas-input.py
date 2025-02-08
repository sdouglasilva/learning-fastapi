from fastapi import FastAPI
from pydantic import BaseModel, EmailStr
from models import User


#Recebendo os dados de uma Request através do BOody
class UserIn(BaseModel):
    name:str
    email:str
    password:str

#importando a classe EmailStr do pydantic
class UserIn(BaseModel):
    name:str
    email:EmailStr
    password:str



users = []
app = FastAPI()

@app.post('/users')
def create_user(user:UserIn):
    #herdando model da classe users e
    new_user = User(**user.model_dump())##criando novo usuário com kwargs - OBJETO para dicionário.
    users.append(new_user)
    return {'message':'Usuário cadastrado com sucesso'}



    