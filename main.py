from acesso_cep import BuscaEndereco
import requests

cep = 15707408

object_cep = BuscaEndereco(cep)

a = object_cep.acessa_via_cep()

print(type(a))
print(a)


# r = requests.get('https://viacep.com.br/ws/01001000/json/')
# print(r)
