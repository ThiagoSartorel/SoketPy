var soap = require('soap');
var url = 'http://localhost:8888/';
var args = {in0: 100, in1: 100};
var cpfes = {cpf: 1}

soap.createClient(url, {}, function(err, client) {
    client.getNumeroSorte(function(err, result) {
        console.log(result);
    });
    client.getSoma(args, function(err, result) {
        console.log(result);
    });
    client.getCPF(cpfes, function(err, result) {
        console.log(result);
    });
});