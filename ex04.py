from fastapi import FastAPI
from fastapi.responses import Response, JSONResponse
# Faça um endpoint onde você passe um numero inteiro via Query Param (o parametro é obrigatório) e retorne um booleano onde será True caso ele seja Par, e False caso seja impar.


app = FastAPI()

@app.get('/is-even{number}')
def is_even(number:int):
  if number % 2 ==0:
    return True
  return False