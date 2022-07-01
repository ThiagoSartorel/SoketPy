package main

import (
	"log"
	"net/http"
	"time"

	"github.com/tiaguinho/gosoap"
)

func main() {
	httpClient := &http.Client{
		Timeout: 1500 * time.Millisecond,
	}
	soap, err := gosoap.SoapClient("http://localhost:8888/", httpClient)
	if err != nil {
		log.Fatalf("SoapClient error: %s", err)
	}
	// Use gosoap.ArrayParams to support fixed position params
	params := gosoap.Params{}
	res, err := soap.Call("getNumeroSorte", params)
	if err != nil {
		log.Fatalf("Call error: %s", err)
	}
	log.Println(res)
	log.Println("-------------------------")

	object := gosoap.Params{
		"numero1": 1,
		"numero2": 2,
	}

	response, err := soap.Call("getSoma", object)
	if err != nil {
		log.Fatalf("Call error: %s", err)
	}
	log.Println(response)
	resposta, err := soap.Call("getCPF", 3)
	if err != nil {
		log.Fatalf("Call error: %s", err)
	}
	log.Println(resposta)
}
