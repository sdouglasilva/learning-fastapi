from enum import Enum
from pydantic import BaseModel

#ENUM CRIA OPÇÕES PARA ESCOLHA
class Genero(str,Enum):
    MASCULINO = 'M'
    FEMININO = 'F'
    OUTRO = 'O'

class Person(BaseModel):
    nome:str
    idade:int
    altura: float
    genero: Genero

person1 = Person(
    nome = 'Douglas',
    idade = 24,
    altura = 1.71,
    genero = Genero.MASCULINO
)
print(person1)