
from Cpf_cnpj import Documento, DocCnpj, DocCpf
from validate_docbr import CNPJ

# num_cpf = Cpf('47032640800')
#
# print(num_cpf)
# # print(num_cpf.validate('44451020832'))


exemplo_cnpj = '36166742000139'

documento = Documento.cria_documento(exemplo_cnpj)

print(documento)


