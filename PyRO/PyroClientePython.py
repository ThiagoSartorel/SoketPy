import Pyro5.api, os


# busca o servidor com base no nome que foi publicado
proxy = Pyro5.api.Proxy("PYRONAME:Abc.Bolinhas")

print('\n<<<<< teste função cpf_valido() >>>>>>>>>')
cpf = input("CPF: ")
print(proxy.cpf_valido(cpf))

