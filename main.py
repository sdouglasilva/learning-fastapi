from fastapi import FastAPI, status
from fastapi.responses import Response, JSONResponse
lista = []
app = FastAPI()


#Método da rota:
# Lista de pessoas
pessoas: list[dict] = [
    {'id': 1, 'nome':'Isa'},
     {'id':2,'nome':'Douglas'} ]

# Endpoint para buscar uma pessoa pelo Id
@app.get('/pessoas/{id}')
def detalhar_pessoa(id: int):
    for pessoa in pessoas:
        if pessoa.get('id') == id:
            return pessoa
    
    return JSONResponse(
		    content={'message': 'Pessoa não encontrada'}, 
		    status_code=status.HTTP_404_NOT_FOUND
		)
            
    


