#SOAP_Cliente_pysimplesoap.py
from pysimplesoap.client import SoapClient
import json

client = SoapClient(wsdl="http://localhost:8888")

print( client.getNumeroSorte() )
print( client.getNumeroSorte()["out0"] )
print( client.getSoma(95,21) )
print( client.getSoma(95,21)["out0"] )