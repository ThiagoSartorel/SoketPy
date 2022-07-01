import Pyro5.api
import random
import os
import base64
import time


@Pyro5.api.expose
class AbcBolinhas(object):

    def cpf_valido(self, cpf: str) -> bool:
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

    def getNumeroSorte(self):
        return random.randint(0, 1000)

    def getSoma(self, a, b):
        return (int(a)+int(b))

    def listarDiretorio(self, dir):
        return os.listdir(dir)

    def salvarArquivo(self, arqEmBase64, nomeArquivo):
        with open(str(time.time())+'_'+nomeArquivo, "wb") as handle:
            handle.write(base64.decodebytes(
                bytes(arqEmBase64.get('data'), 'utf-8')))
            return True


daemon = Pyro5.api.Daemon()
ns = Pyro5.api.locate_ns()         # find the name server
# antes de executar o servidor é necessário executar o servidor de nomes
# python -m Pyro5.nameserver
uri = daemon.register(AbcBolinhas)
# register the object with a name in the name server
ns.register("Abc.Bolinhas", uri)

# imprime o uri para que possamos usá-lo no cliente mais tarde
print("Object uri =", uri)
# inicia o loop de eventos do servidor para esperar por chamadas
daemon.requestLoop()


'''
pip install Pyro5

Executar o servidor de nomes
python -m Pyro5.nameserver

Executar o servidor e os clientes
python PyroServidorPython.py
python PyroClientePython.py

'''
