import pytest

from libpythonph.spam.criar_enviador_email import Enviador
from libpythonph.spam.main import EnviadorDeSpam
from libpythonph.spam.modelos import Usuario


@pytest.mark.parametrize(
    'usuarios',
    [
        [
            Usuario(nome='Pedro',email='pedro@solucoesweb.com'),
            Usuario(nome='Luciano',email='luciano@solucoesweb.com')
        ],
        [
            Usuario(nome='Pedro',email='pedro@solucoesweb.com')
        ]
    ]
)
def test_qtd_de_spam(sessao, usuarios):
    for usuario in usuarios:
        sessao.salvar(usuario)
    enviador = Enviador()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'pedro@solucoesweb.com.br',
        'assunto',
        'corpo do email'
    )
    assert len(usuarios) == enviador.qtd_email_enviados
