from pydantic import BaseModel
from uuid import UUID, uuid4


class MessageOut(BaseModel):
    message:str


class CarIn(BaseModel):
    marca:str
    modelo:str
    ano:int
    placa: str
    kilometragem: int

class CarOut(BaseModel):
    id: UUID = uuid4()
    marca:str
    modelo:str
    ano:int
    placa: str
    kilometragem: int

    

