<?php
$client = new SoapClient("http://localhost:8888/");

$params = array(
    "num1" => 100,
    "num2" => 200
);

$cpf = array(
    "cpf" => 1,
);

$response = $client->__soapCall("getNumeroSorte", $params);
echo $response;

$response = $client->__soapCall("getSoma", array($params));
echo $response;

$response = $client->__soapCall("getCPF", $cpf);
echo $response;
?>