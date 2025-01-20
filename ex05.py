# Utilize os conhecimentos aprendidos nessa aula para implementar uma API de Sorteio! Siga os passos a seguir:

#A) Implemente um endpoint que recebe um nome via Path Param, e adiciona o nome em uma lista de nomes.

from fastapi import FastAPI, status
from fastapi.responses import JSONResponse

app = FastAPI()

participants =[]

@app.post('/sorteio/{name}/adicionar')
def add_participant(name:str):
  participants.append(name)
  return JSONResponse({
    "message":"Participante adicionado com sucesso"
  })
