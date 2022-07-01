import os
import xmlrpc.client

with xmlrpc.client.ServerProxy("http://localhost:8000/") as proxy:

    print('\n<<<<< teste função valida_cpf() >>>>>>>>>')
    cpf = input("Digite o cpf: ")
    print("Seu número da sorte é: {0}.".format(proxy.cpfValido("08860883997")))


