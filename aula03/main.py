from fastapi import FastAPI
from models import User
from schemas import UserIn, UserOut





users = []
app = FastAPI()

@app.get('/users')
def get_all_users()->list[UserOut]:
    return users


@app.post('/users')
def create_new_users(user:UserIn):
    print(user.model_dump())
    new_user = User(**user.model_dump())#OBJETO para dicionário/JSON
    users.append(new_user)
    print(users)
    return {'message':'Usuário Cadastrado com Sucesso'}