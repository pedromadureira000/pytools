from unittest.mock import Mock
import pytest
from libpythonph import git_hubapi


@pytest.fixture
def avatar_url():
    resp_mock = Mock()
    url = 'https://avatars.githubusercontent.com/u/402714?v=4'
    resp_mock.json.return_value = {
        'login': 'renzo', 'id': 402714,
        'avatar_url': url
    }
    # vc atribui um Mock a um metodo get da biblioteca requests que foi importada para para o pacote libpythonph que vc
    # importou no escopo desse codigo.
    get_original = git_hubapi.requests.get
    git_hubapi.requests.get = Mock(return_value=resp_mock)
    yield url
    git_hubapi.requests.get = get_original

def test_buscar_avatar(avatar_url):
    url = git_hubapi.buscar_avatar('renzo')
    assert avatar_url == url

def test_buscar_avatar_integracao():
    url = git_hubapi.buscar_avatar('renzoN')
    assert 'https://avatars.githubusercontent.com/u/3457115?v=4' == url
