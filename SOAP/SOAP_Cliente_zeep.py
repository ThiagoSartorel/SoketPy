#SOAP_Cliente_zeep.py
import zeep

client = zeep.Client(wsdl='http://127.0.0.1:8888')

print( client.service.getNumeroSorte() )
print( client.service.getSoma(95,32) )