from pydantic import BaseModel
from uuid import UUID, uuid4

class CarIn(BaseModel):
    marcar:str
    modelo:str
    ano:int
    placa: str
    kilometragem: int

class CarOut(BaseModel):
    id: UUID
    modelo:str
    ano:int
    placa: str
    kilometragem: int

    

