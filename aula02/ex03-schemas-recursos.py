from fastapi import FastAPI
from uuid import UUID, uuid4
from pydantic import BaseModel
from datetime import datetime, timezone

#Criando a classe para representar usuários da aplicação
class User(BaseModel):
    id: UUID = uuid4()# Campo id do tipo UUID = valor padrão retorno da função uuid4
    name: str
    

