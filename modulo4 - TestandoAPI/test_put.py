import requests

headers = {'Authorization': 'Token 2b84090c545c134c329e42327863b4890cb61083'}

url_base_cursos = 'http://localhost:8000/api/v2/cursos/'
url_base_avaliacoes = 'http://localhost:8000/api/v2/avaliacoes/'


curso_atualizado = {
    'titulo': 'Curso de Gestão em Scrum Completo',
    'url': 'http://www.gestaoemscrumcompleto.com.br'
}

# Buscando curso de ID 6
# buscar = requests.get(url=f'{url_base_cursos}6/', headers=headers)
# print(buscar.json())


resultado = requests.put(url=f'{url_base_cursos}6/', headers=headers, data=curso_atualizado)

# Testando status code de retorno
assert resultado.status_code == 200

# Testando o retorno do titulo
assert resultado.json()['titulo'] == curso_atualizado['titulo']
