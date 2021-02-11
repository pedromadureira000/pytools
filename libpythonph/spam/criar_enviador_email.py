class Enviador:
    def __init__(self):
        self.qtd_email_enviados = 0

    def enviar(self, destinatario, remetente, assunto, corpo):
        if '@' not in destinatario:
            raise EmailInvalido(f"Email de destinatario invalido {destinatario}")
        self.qtd_email_enviados += 1
        return destinatario


class EmailInvalido(Exception):
    pass