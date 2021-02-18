import pytest
from libpythonph.spam.db import Conexao


# o decorator fixture do pytest executa a função e traz o resultado para o parametro da função o chamar
# o yield cria uma função geradora
@pytest.fixture(scope='session')
def conexao():
    # setup
    conexao_obj = Conexao()
    yield conexao_obj
    # tierdown
    conexao_obj.fechar()


# uma fixture pode depender de outra
@pytest.fixture
def sessao(conexao):
    # setup
    sessao_obj = conexao.gerar_sessao()
    yield sessao_obj
    # tierdown
    sessao_obj.roll_back()
    sessao_obj.fechar()
