from fastapi import FastAPI, status
from models import Person
from schemas import PersonIn,MessageOut
from pydantic import BaseModel
from pydantic import ValidationError
from fastapi.responses import JSONResponse


persons = []
app  = FastAPI()

@app.get('/pessoas/listar',response_model=MessageOut)
def list_all_persons():
  try:
      return JSONResponse(content=persons, status_code=status.HTTP_200_OK)
  except ValidationError as error:
      if len(persons) == 0:
        return {"message":f'Nenhuma pessoa cadastrada na lista{error}'}
      
@app.post('/pessoas/cadastrar', response_model=MessageOut)
def create_new_person(person:PersonIn)-> MessageOut:
    try:  
      new_person = Person(**person.model_dump())
      persons.append(new_person)

      return {'message':'Pessoa cadastrada com sucesso'}
    except ValidationError as error:
      return {"message":f"Erro de validação{error}"}
    
