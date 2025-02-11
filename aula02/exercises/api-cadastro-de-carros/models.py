from pydantic import BaseModel

class Car(BaseModel):
    marca:str
    modelo:str
    ano: int
    placa: str
    kilometragem: int

    