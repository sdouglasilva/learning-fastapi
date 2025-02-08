from fastapi import FastAPI, HTTPException, status
from models import User
from schemas import UserIn, UserOut, MessageOut
import db




users = []
app = FastAPI()

@app.get('/users')
def get_all_users()->list[UserOut]:
    users = db.get_all_users()
    if len(users) == 0:
        raise HTTPException(status.HTTP_204_NO_CONTENT)

    return users


@app.post('/users',response_model=MessageOut)
def create_new_users(user:UserIn)->  MessageOut:

    print(user.model_dump())
    new_user = User(**user.model_dump())#OBJETO para dicionário/JSON
    users.append(new_user)
    db.create_new_user(new_user)
    print(users)
    return {'message':'Usuário Cadastrado com Sucesso'}