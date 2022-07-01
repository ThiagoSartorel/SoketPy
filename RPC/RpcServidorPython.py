import os
import random
import time
from xmlrpc.server import SimpleXMLRPCServer

def cpf_valido(cpf: str) -> bool:
    TAMANHO_CPF = 11
    if len(cpf) != TAMANHO_CPF:
        return False

    if cpf in (c * TAMANHO_CPF for c in "1234567890"):
        return False

    cpf_reverso = cpf[::-1]
    for i in range(2, 0, -1):
        cpf_enumerado = enumerate(cpf_reverso[i:], start=2)
        dv_calculado = sum(map(lambda x: int(x[1]) * x[0], cpf_enumerado)) * 10 % 11
        if cpf_reverso[i - 1:i] != str(dv_calculado % 10):
            return False

    return True


def getNumeroSorte():
    return random.randint(0, 1000)


def getSoma(a, b):
    return (int(a)+int(b))


def listarDiretorio(dir):
    return os.listdir(dir)


def salvarArquivo(arqEmBase64, nomeArquivo):
    with open(str(time.time())+'_'+nomeArquivo, "wb") as handle:
        handle.write(arqEmBase64.data)
        return True


server = SimpleXMLRPCServer(("localhost", 8000))
print("Listening on port 8000...")

server.register_function(cpf_valido, "cpfValido")
server.register_function(getNumeroSorte, "getNumeroSorte")
server.register_function(getSoma, "getSoma")
server.register_function(listarDiretorio, "listarDiretorio")
server.register_function(salvarArquivo, "salvarArquivo")

server.serve_forever()
