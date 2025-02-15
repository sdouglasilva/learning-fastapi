from fastapi import FastAPI, status
from fastapi.responses import JSONResponse
from schemas import CarIn



cars_list = []
app = FastAPI()

@app.post("/carros")
def add_car(car:CarIn):
    carro1 = CarIn("Ford","Ka",2020,"AAA0001",50000)
    cars_list.append(carro1)
    return JSONResponse(content=cars_list,status_code=status.HTTP_200_OK)





    

@app.get('/carros')
def view_cars():
    pass


