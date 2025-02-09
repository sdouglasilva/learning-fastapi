# Ex. 01- Cadastro de Pessoas
## Faça uma API para gerenciar pessoas. Sua API deve ter poder cadastrar e listar pessoas, salve as pessoas em uma lista de dicionários.
### Implemente um endpoint para cadastrar uma pessoa.
```
POST - /pessoas
Request Body
{
	"nome": "Lorem",
	"idade": 20,
	"altura": 1.62,
	"genero": "M"
}
O genero deve ser do tipo ENUM e aceitar somente os valores “M” (Masculino), “F” (Feminino) ou “O” (Outro)
  
```​
Response
{
	"message": "Pessoa cadastrada com sucesso."
}
​
Implemente um endpoint para listar pessoas
GET - /pessoas
Response
[
	{
		"nome": "Lorem",
		"idade": 20,
		"altura": 1.72,
		"genero": "M"
	}
]