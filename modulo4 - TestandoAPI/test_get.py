import requests

headers = {'Authorization': 'Token 2b84090c545c134c329e42327863b4890cb61083'}

url_base_cursos = 'http://localhost:8000/api/v2/cursos/'
url_base_avaliacoes = 'http://localhost:8000/api/v2/avaliacoes/'

resultado = requests.get(url=url_base_cursos, headers=headers)
#print(resultado)


# Testando se o endpoint cursos está correto
assert resultado.status_code == 200

# Testando se o titulo do primeiro curso está correio
assert resultado.json()['results'][0]['titulo'] == 'Programação para Web'

