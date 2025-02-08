#Implemente um endpoint que retorna um JSON mostrando uma mensagem de “Olá Mundo”. Exemplo:
from fastapi import FastAPI

app = FastAPI()

@app.get('/home')
def root():
    return{'message: Olá mundo'}