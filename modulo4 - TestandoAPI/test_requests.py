import requests

# GET Avaliações (Retorno de todas as avaliacões)
# avaliacoes = requests.get('http://localhost:8000/api/v2/avaliacoes')


# Acessando o status code do request avaliacoes
# print(avaliacoes.status_code)

# Acessando os dados/Tipo do Response
# print(avaliacoes.json())
# print(type(avaliacoes.json())) # O retorno é do tipo dicionário

# Retornando a quantidade de registro  ['count']
# print(avaliacoes.json()['count'])

# Retornando link da proxima página de registro  ['next']
# print(avaliacoes.json()['next'])

# Acessando os resultados dos registro  ['results']
# print(avaliacoes.json()['results'])
# print(type(avaliacoes.json()['results']))

# Acessando o primeiro elemento da lista
# print(avaliacoes.json()['results'][0])

# Acessando o último elemento da lista
# print(avaliacoes.json()['results'][-1])

# Acessando um campo do primeiro elemento da lista
# print(avaliacoes.json()['results'][0]['nome'])


# GET Avalição (Retorno de uma avaliação específica)
# avaliacao = requests.get('http://localhost:8000/api/v2/avaliacoes/4/')
# print(avaliacao.json())

# GET Cursos (Retornando cursos)

# Se antenticando e acessando cursos
# headers = {'Authorization': 'Token 2b84090c545c134c329e42327863b4890cb61083'}
# cursos = requests.get(url='http://localhost:8000/api/v2/cursos/', headers=headers)
# print(cursos.status_code)



