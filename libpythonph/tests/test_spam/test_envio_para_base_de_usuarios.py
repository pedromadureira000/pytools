from unittest.mock import Mock

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
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'pedro@solucoesweb.com',
        'assunto',
        'corpo do email'
    )
    assert len(usuarios) == enviador.enviar.call_count


def test_paramentros_de_spam(sessao):
    usuario = Usuario(nome='Pedro',email='pedro@solucoesweb.com')
    sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'luciano@solucoesweb.com.br',
        'assunto',
        'corpo do email'
    )
    assert enviador.enviar.asset_called_once_with(
        'luciano@solucoesweb.com.br',
        'pedro@solucoesweb.com',
        'assunto',
        'corpo do email'

    )