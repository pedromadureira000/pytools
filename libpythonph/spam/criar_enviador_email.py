class Enviador:

    def enviar(self, destinatario, remetente, assunto, corpo):
        if '@' not in destinatario:
            raise EmailInvalido(f"Email de destinatario invalido {destinatario}")
        return destinatario


class EmailInvalido(Exception):
    pass