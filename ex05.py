# Utilize os conhecimentos aprendidos nessa aula para implementar uma API de Sorteio! Siga os passos a seguir:

#A) Implemente um endpoint que recebe um nome via Path Param, e adiciona o nome em uma lista de nomes.
import random
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

# B) Implemente um endpoint que retorna o nome de todos os participantes do sorteio em uma lista. Caso não haja participantes, deve retornar uma resposta vazia e com o status code 204.

@app.get('/sorteio/participantes')
def get_all_participants():
  if participants != '':
    return JSONResponse(content=participants,status_code=status.HTTP_200_OK)
  return JSONResponse({}, status_code=status.HTTP_204_NO_CONTENT)

# C) Adicione um parametro de busca chamado “search” via Query Param que trás todos os nomes que o valor passado está presente no nome.

@app.get('/participants')
def list_participants(search:str | None = None):
  #Se a busca não for vazia. cria-se uma lista vazia
  if search is not None:
    result = []
    #Iteramos sobre a lista e verificamos se os caracteres de busca desejados estão presentes na lsita de participantes.
    for participant in participants:
      if search.upper() in participant.upper():
        result.append(participant)
    return result
  return participants


# D) Implemente um endpoint que limpe a lista dos participantes do sorteio.
@app.delete('/sorteio/limpar')
def remove_all_participants():
  participants.clear()
  return JSONResponse({"message":"Lista de participantes limpa com sucesso."} )

# E) Implemente um endpoint que sorteia e retorna o participante sorteado
@app.get('/sorteio/executar')
def sort_participant():
  sorted_participant = random.choice(participants)
  return JSONResponse({"result": sorted_participant})