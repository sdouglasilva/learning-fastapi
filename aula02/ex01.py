from fastapi import FastAPI
from pydantic import BaseModel

class Person(BaseModel):
    name:str
    age:int
    height:float
    active:bool = True #Implementando valor padrão
    skills: list[str] = [] #Lista vazia como valor padrão

person1 = Person(
    name='Douglas',
    age='21',#realiza conversão de tipo automática.
    height=1.71,
    skills=['SystemAnalicts','Teaching']
)


print(person1)

#Convertendo Objeto Pydantic para JSON - str
json_data = person1.model_dump_json(indent=2)
print(json_data)
print(type(json_data))


#Convertendo JSON para dicionário python - dict
dict_data = person1.model_dump()
print(dict_data)
print(type(dict_data))


json_data_for_dantic  ='''
{
    "name": "Douglas",
    "age": 24,
    "height": 1.71,
    "active": true,
    "skills": [
        "SystemAnalitcs",
        "Teaching"
    ]
}
'''

#Convertendo ObjetoPydantic para um modelo python
#Crio um variável que recebe a classe do modelo, chamo o método model_validate_json, depois passo como argumento a variável que contém o valor que quero converte.
dantic_data = Person.model_validate_json(json_data_for_dantic)
print(dantic_data)
print(type(dantic_data))#saída: <class '__main__.Person'>

