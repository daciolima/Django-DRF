import requests


url_base_avaliacoes = 'http://localhost:8000/api/v2/avaliacoes/'

resultado = requests.delete(url=f'{url_base_cursos}6/', headers=headers)

# Testando status code
assert resultado.status_code == 204

# print(resultado.text)

# Testando se o tamanho conteúdo do retorno é 0
assert len(resultado.text) == 0
