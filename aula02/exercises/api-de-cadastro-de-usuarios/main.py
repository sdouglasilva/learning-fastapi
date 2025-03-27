from fastapi import FastAPI
from models import User
from uuid import UUID
from schemas import UserIn, UserOut, MessageOut
from uuid import UUID

app = FastAPI()

users_list:list[User] = []

@app.post("/usuarios")
def cadastrar_usuario(user:UserIn)->MessageOut:
    for user_in_db in users_list:
        if user.email == user_in_db.email:
            return MessageOut(message='Email já cadastrado, tente novamente.')

    new_user = User(**user.model_dump())
    users_list.append(new_user)
    return MessageOut(message='Usuário cadastrado com sucesso')

@app.get('/usuarios')
def listar_todos_usuarios()->list[UserOut]:
    if len(users_list) == 0:
        return []
    return users_list

@app.get('/usuarios/nome:{nome_de_usuario}')
def listar_usuario(nome_de_usuario:str)-> UserOut:
    for user_in_db in users_list:
        if user_in_db.nome == nome_de_usuario:
            return user_in_db

@app.get('/usuarios/id:{uuid}', response_model=UserOut)
def listar_usuario_uuid(uuid:UUID)->UserIn:
    for user_in_db in users_list:
        if user_in_db.id == uuid:
            return user_in_db


@app.put('/alterar/usuario/{uuid}')
def alterar_info_usuario(uuid:UUID, usuario:UserOut)-> MessageOut:
     for user_in_db in users_list:
        if user_in_db.id == uuid:
            user_in_db.nome = usuario.nome
            user_in_db.email = usuario.email
            return MessageOut(message="Usuário alterado com sucesso")


@app.delete('/deletar/{uuid}/usuario')
def deletar_usuario(uuid:UUID)-> MessageOut:
    for user_in_db in users_list:
        if user_in_db.id == uuid:
            users_list.remove(user_in_db)
            return users_list, MessageOut(message="Usuário removido com sucesso")
            
    return MessageOut(message="Usuário não encontrado")






    