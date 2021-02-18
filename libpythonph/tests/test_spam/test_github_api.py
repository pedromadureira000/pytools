from unittest.mock import Mock

from libpythonph import git_hubapi


def test_buscar_avatar():
    resp_mock = Mock()
    resp_mock.json.return_value = {
        'login': 'renzo', 'id': 402714,
        'avatar_url': 'https://avatars.githubusercontent.com/u/402714?v=4'
    }
    #vc atribui um Mock a um metodo get da biblioteca requests que foi importada para para o pacote libpythonph que vc
    #importou no escopo desse codigo.
    git_hubapi.requests.get = Mock(return_value=resp_mock)
    url = git_hubapi.buscar_avatar('renzo')
    assert 'https://avatars.githubusercontent.com/u/402714?v=4' == url