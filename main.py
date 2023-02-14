
from Cpf_cnpj import CpfCnpj
from validate_docbr import CNPJ

# num_cpf = Cpf('47032640800')
#
# print(num_cpf)
# # print(num_cpf.validate('44451020832'))


exemplo_cnpj = '15485485487854'

documento = CpfCnpj(exemplo_cnpj, 'cnpj')

print(documento)


