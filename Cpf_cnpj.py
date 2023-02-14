from validate_docbr import CPF, CNPJ


class CpfCnpj:

    def __init__(self, documento, tipo):
        self.tipo = tipo
        documento = str(documento)
        if self.tipo == 'cpf':
            if self.cpf_valido(documento):
                self.cpf = documento
            else:
                raise ValueError('CPF inválido.')
        elif self.tipo == 'cnpj':
            if self.cnpj_valido(documento):
                self.cnpj = documento
            else:
                raise ValueError('CNPJ inválido.')
        else:
            raise ValueError('Não é um documento válido.')

    def cpf_valido(self, cpf):
        if len(cpf) == 11:
            validador = CPF()
            return validador.validate(cpf)
        else:
            raise ValueError('Quantidade de digitos inválida.')

    def __str__(self):
        if self.tipo == 'cpf':
            return self.format_cpf()
        elif self.tipo == 'cnpj':
            return self.format_cnpj()

    def format_cpf(self):
        mascara = CPF()
        return mascara.mask(self.cpf)

    def format_cnpj(self):
        mascara = CNPJ()
        return mascara.mask(self.cnpj)

    def cnpj_valido(self, cnpj):
        if len(cnpj) == 14:
            validate_cnpj = CNPJ()
            return validate_cnpj.validate(cnpj)
        else:
            raise ValueError('Quantidade de digitos inválida.')

