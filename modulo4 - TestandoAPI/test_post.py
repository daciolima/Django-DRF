import requests


url_base_cursos = 'http://localhost:8000/api/v2/cursos/'
url_base_avaliacoes = 'http://localhost:8000/api/v2/avaliacoes/'

novo_curso = {
    'titulo': 'Curso Gestão em Scrum',
    'url': 'http://www.gestaoemscrum.com.br'
}

headers = {'Authorization': 'Token 2b84090c545c134c329e42327863b4890cb61083'}

resultado = requests.post(url=url_base_cursos, headers=headers, data=novo_curso)

# Testando o retorno do status code
assert resultado.status_code == 201

# Testando se o titulo retornado é o mesmo que foi informado
assert resultado.json()['titulo'] == novo_curso['titulo']


