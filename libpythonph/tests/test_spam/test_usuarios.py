import pytest
from libpythonph.spam.db import Conexao
from libpythonph.spam.modelos import Usuario

@pytest.fixture
def conexao():
    #setup
    conexao_obj = Conexao()
    yield conexao_obj
    #tierdown
    conexao_obj.fechar()
#o decorator fixture do pytest executa a função e traz o resultado para o argumento da linha 10
#o yield cria uma função geradora

@pytest.fixture(scope='session')
def sessao(conexao):
    #setup
    sessao_obj = conexao.gerar_sessao()
    yield sessao_obj
    #tierdown
    sessao_obj.roll_back()
    sessao_obj.fechar()
#uma fixture pode depender de outra

def test_salvar_usuario(sessao):
    usuario = Usuario(nome='Pedro')
    sessao.salvar(usuario)
    assert isinstance(usuario.id, int)

def test_listar_usuarios(sessao):
    usuarios = [Usuario(nome='Pedro'), Usuario(nome='Luciano')]
    for usuario in usuarios:
        sessao.salvar(usuario)
    assert usuarios == sessao.listar()

