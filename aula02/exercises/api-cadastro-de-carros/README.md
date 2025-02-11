### Faça uma API para cadastrar carros. Sua API deve ter poder cadastrar e listar carros, salve os carros em uma lista de dicionários.

## ``1.`` Implemente um endpoint para cadastrar um usuário, ao cadastrar o seu programa deve criar um ``ID`` e seguir algumas ``regras``:

```
POST - /carros
Request Body
{
	"marca": "Ford",
	"modelo": "Ka",
	"ano": 2020,
	"placa": "AAA0001",
	"kilometragem": 50000
}
​
Response
{
	"message": "Carro cadastrada com sucesso."
}
​
Implemente um endpoint para listar carros.
GET - /carros
Response
[
	{
		"id": 1,
		"marca": "Ford",
		"modelo": "Ka",
		"ano": 2020,
		"placa": "AAA0001",
		"kilometragem": 50000
	}
]
```