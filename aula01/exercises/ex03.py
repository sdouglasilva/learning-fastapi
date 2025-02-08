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
##Criação da rota para buscar todos os animais da lista
@app.get('/animais')
def listar_todos_animais():
    """Função para listar todos os animais
    """
    #Se o tamanho da lista for igual a  ele retorna um erro, se não ele retonra uma resposta em JSON.
    if len(animais) == 0:
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    return JSONResponse(content=animais, status_code=status.HTTP_200_OK)
##Criação da rota para busar um animal espefífico da lista.
@app.get('/animais/{id}')#{id}Path
def listar_animal_especifico(id:int):#Query
    """Função para percorrer a lista de animais
    """
    #Para cada animal na lista, verifica se o parametro é igual a query desejada.
    for animal in animais:
        ### animal.get('id') - Query
        ### id - Path
        if animal.get('id') == id:
            return animal
    return JSONResponse(
        content = {'message':'Animal não encontrado'},
        status_code = status.HTTP_404_NOT_FOUND)