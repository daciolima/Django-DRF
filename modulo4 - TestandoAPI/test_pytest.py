import requests


class TestCursos:
    headers = {'Authorization': 'Token 2b84090c545c134c329e42327863b4890cb61083'}
    url_base_cursos = 'http://localhost:8000/api/v2/cursos/'

    def test_get_cursos(self):
        cursos = requests.get(url=self.url_base_cursos, headers=self.headers)
        assert cursos.status_code == 200

    def test_get_curso(self):
        curso = requests.get(url=f'{self.url_base_cursos}5/', headers=self.headers)
        assert curso.status_code == 200

    def test_post_curso(self):
        novo = {
            'titulo': 'Curso de RubyOnRaisl',
            'url': 'http://www.cursorubyonrailsfull.com'
        }

        resultado = requests.post(url=self.url_base_cursos, headers=self.headers, data=novo)

        assert resultado.status_code == 201
        assert resultado.json()['titulo'] == novo['titulo']

    def test_put_curso(self):
        curso_atualizando = {
            'titulo': 'Curso de Javascript Completo FULL',
            'url': 'http://www.cursojavascript.com'
        }

        resultado = requests.put(url=f'{self.url_base_cursos}12/', headers=self.headers, data=curso_atualizando)

        assert resultado.status_code == 200

    def test_delete_curso(self):
        resultado = requests.delete(url=f'{self.url_base_cursos}12/', headers=self.headers)

        assert resultado.status_code == 204 and len(resultado.text) == 0



