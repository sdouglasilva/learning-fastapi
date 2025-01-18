#Implemente um endpoint que retorne uma string que deve conter uma tag HTML de título (<h1>). Exemplo:
from fastapi import FastAPI, status
from fastapi.responses import HTMLResponse

app = FastAPI()
@app.get('/home')
def exibir_titulo():
    return HTMLResponse('<H1>Títutlo do Meu Site</H1>')

