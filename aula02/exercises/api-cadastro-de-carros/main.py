from fastapi import FastAPI, status
from fastapi.responses import JSONResponse
from models import Car
from schemas import CarIn

app = FastAPI()

lista_de_carros = []

carro1 = CarIn("Ford","Ka",2020,"AAA0001",50000)

print(carro1)
@app.post("/carros")
def add_car():
    if carro1.placa not in lista_de_carros:
        lista_de_carros.append(carro1)
        return JSONResponse(status_code=status.HTTP_200_OK)
    return JSONResponse(content=lista_de_carros, status_code=status.HTTP_204_NO_CONTENT)


    

@app.get('/carros')
def view_cars():
    pass


