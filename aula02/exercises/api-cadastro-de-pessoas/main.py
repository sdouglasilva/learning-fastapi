from fastapi import FastAPI, status
from schemas import PersonIn,MessageOut

from fastapi.responses import JSONResponse


persons = [{
  "name": "string",
  "age": 0,
  "heigth": 0,
  "gender": "M"
}]
app  = FastAPI()

@app.get('/pessoas/listar',response_model=MessageOut)
def list_all_persons() ->MessageOut:
  if not persons:
     return JSONResponse(content={"message":"Nenhuma pessoa cadastrada"},status_code=status.HTTP_204_NO_CONTENT)
  print(persons)
  return JSONResponse(content={"pessoas":[person for person in persons]},status_code=status.HTTP_200_OK)
     
      
@app.post('/pessoas/cadastrar', response_model=MessageOut)
def create_new_person(person:PersonIn)-> MessageOut:
    new_person = person.model_dump()
    persons.append(new_person)

    return MessageOut(message="Pessoa cadastrada com sucesso.")

    
