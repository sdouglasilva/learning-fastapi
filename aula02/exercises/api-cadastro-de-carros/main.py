from fastapi import FastAPI, status
from fastapi.responses import JSONResponse
from schemas import CarIn, MessageOut, CarOut
from models import Car



cars_list = []
app = FastAPI()

@app.post("/carros")
def add_car(car:CarIn) -> MessageOut:
    carro1 = Car(**car.model_dump())
    cars_list.append(carro1)
    return MessageOut(message="Carro cadastrado com sucesso!")

@app.get('/carros')
def view_all_cars()-> list[CarOut]:
    if len(cars_list) == 0:
        return MessageOut(message="Nenhum carro disponível para visulização")
    return cars_list


