#Crie uma aplicação com uma lista com 4 animais
#Depois, implemente um endpoint utilizando o FastAPI que receba um numero inteiro via Path Param (o ID) e retorne o animal correspondente, caso o animal não seja encontrado retorne uma resposta com status code (404, Not Found)

from fastapi import FastAPI, status
from fastapi.responses import Response, JSONResponse

app = FastAPI()

animais = [
    {
        'id':1,
        'nome':'Lily',
        'especie':'Gato'
    },
    {
        'id':2,
        'nome':'Torby',
        'especie':'Cachorro'
    },
    {
        'id':3,
        'nome':'Fani',
        'especie':'Gato'
    },
    {
        'id':4,
        'nome':'Josefina',
        'especie':'Papagaio'
    },
    
]

@app.get('/animais')
def listar_todos_animais():
    if len(animais) == 0:
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    return JSONResponse(content=animais, status_code=status.HTTP_200_OK)