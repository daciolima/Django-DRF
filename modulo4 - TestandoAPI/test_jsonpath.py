import requests
import jsonpath

avaliacoes = requests.get('http://localhost:8000/api/v2/avaliacoes')

# todos = jsonpath.jsonpath(avaliacoes.json(), 'results')
# print(todos)

# primeira_avaliacao = jsonpath.jsonpath(avaliacoes.json(), 'results[0]')
# print(primeira_avaliacao)

# campo_avaliacao = jsonpath.jsonpath(avaliacoes.json(), 'results[0].nome')
# print(campo_avaliacao)

# curso_id = jsonpath.jsonpath(avaliacoes.json(), 'results[0].avaliacao')
# print(curso_id)

# Retornando todos os nome que avaliaram
nomes = jsonpath.jsonpath(avaliacoes.json(), 'results[*].nome')
print(nomes)
