from zeep import Client

client = Client('http://127.0.0.1:8888')
print(client.service.getNumeroSorte())
print(client.service.getSoma(100, 200))
print(client.service.getCPF(1))