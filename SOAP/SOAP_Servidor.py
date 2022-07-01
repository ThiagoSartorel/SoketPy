# SOAP_Servidor.py
import random
from pysimplesoap.server import SoapDispatcher, SOAPHandler, WSGISOAPHandler

# métodos com as implementações da operação/serviço
def getNumeroSorte():
    return random.randint(0, 1000)
def getSoma(in0, in1):
    print (in0, in1)
    return in0 + in1
def getCPF(cpf):
    return True if cpf == 1 else False

# criação do objeto soap
dispatcher = SoapDispatcher(
    'AbcBolinhas',
    location='http://localhost:8888/',
    action='http://localhost:8888/',
    namespace="http://localhost:8888/", prefix="ns0",
    documentation='Exemplo usando SOAP através de PySimpleSoap',
    trace=True, debug=True, ns=True)
# publicação dos serviços, com seu alias, retorno e parâmetros
dispatcher.register_function('getNumeroSorte', getNumeroSorte, returns={'out0': int}, args={})
dispatcher.register_function('getSoma', getSoma, returns={'out0': int}, args={'in0': int, 'in1': int})
dispatcher.register_function('getCPF', getCPF, returns={'out0': bool}, args={'cpf': int})

if __name__ == '__main__':
    print ("Starting server...")
    from http.server import HTTPServer
    httpd = HTTPServer(("", 8888), SOAPHandler)
    
    httpd.dispatcher = dispatcher
    httpd.serve_forever()