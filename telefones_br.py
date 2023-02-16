import re


class TelefoneBr:

    def __init__(self, string):
        if self.valida_telefone(string):
            self._telefone = string
        else:
            raise ValueError('Número inválido.')

    def valida_telefone(self, string):
        padrao = re.compile('([0-9]{2,3}?)?([1-9]{2})([6-9])?([0-9]{4})([0-9]{4}$)')
        buscador = re.search(padrao, string)
        if buscador:
            return True
        else:
            return False

    @property
    def _numero_formatado(self):
        padrao = "([0-9]{2,3}?)?([1-9]{2})([6-9])?([0-9]{4})([0-9]{4}$)"
        telefone = re.search(padrao, self._telefone)
        return telefone.group


    def __str__(self):
        cod = self._numero_formatado
        if not cod(1) and not cod(3):
            return f'({cod(2)}) {cod(4)}-{cod(5)}'
        elif not cod(1):
            return f'({cod(2)}) {cod(3)}{cod(4)}-{cod(5)}'
        elif not cod(3):
            return f'+{cod(1)} ({cod(2)}) {cod(4)}-{cod(5)}'
        else:
            return f'+{cod(1)} ({cod(2)}) {cod(3)}{cod(4)}-{cod(5)}'

