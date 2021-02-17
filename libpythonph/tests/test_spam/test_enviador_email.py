import pytest

from libpythonph.spam.criar_enviador_email import Enviador, EmailInvalido


def test_criar_enviador_email():
    enviador = Enviador()
    assert enviador is not None


#usando o decorator @pytest.mark.paramatrize, vc vai escolher um parametro(nome de variavel) e uma lista de valores que
#serão testados, passando-os como argumento pro parametro
@pytest.mark.parametrize(
    'destinatario',['joaozinho@gmail.com','lerolero@aa.com']
)
def test_remetente(destinatario):
    enviador = Enviador()
    destinatarios = ['joaozinho@gmail.com','lerolero@aa.com']
    resultado = enviador.enviar(
        destinatario,
        'pedrinho@gmail.com',
        'Assunto',
        'corpo da mensagem')
    assert destinatario in resultado


@pytest.mark.parametrize(
    'destinatario',['','lerolero']
)
def test_remetente_invalido(destinatario):
    enviador = Enviador()
    destinatarios = ['joaozinho@gmail.com','lerolero@aa.com']
    #gerenciador de contexto
    with pytest.raises(EmailInvalido):
        enviador.enviar(
            destinatario,
            'pedrinho@gmail.com',
            'Assunto',
            'corpo da mensagem'
        )
