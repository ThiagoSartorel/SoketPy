var soap = require('soap');
var url = 'http://localhost:5000';

soap.createClient('http://localhost:5000/user/0', {}, function(err, client) {
    console.log();
})