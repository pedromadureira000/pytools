from libpythonph.spam.criar_enviador_email import Enviador
from libpythonph.spam.main import EnviadorDeSpam


def test_envio_de_spam(sessao):
    enviador_de_spam = EnviadorDeSpam(sessao, Enviador())
    enviador_de_spam.enviar_emails(
        'pedro@solucoesweb.com.br',
        'assunto',
        'corpo do email'
    )
