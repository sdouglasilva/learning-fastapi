from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class MessageReponse(BaseModel):
    message:str


@app.get('/')
def hello_word():
    #Retornando uma mensagem personalizada com base na classe criada pelo pydantic
    return MessageReponse(message='Hello World')

#retornando uma resposta no formato de dicionário
@app.get('/dict', response_model=MessageReponse)
def return_dict_message():
    return {'message':'Hello World'}

#retornando uma reposta do formato de objeto
@app.get('/object')
def return_object_message()->MessageReponse:
    return{'message':'Hello World'}




