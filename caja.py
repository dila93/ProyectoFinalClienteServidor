from BaseHTTPServer import  BaseHTTPRequestHandler, HTTPServer

import urllib
import urllib2
import json

#data = simplejson.loads(response)

productos = ["panela", "arroz","chorizo","mantequilla","chocolate","carne","arepas", "huevos"]
print productos
print "\n"



menu = True
while (menu == True):

	print("1. listar productos")
	print("2. informacion del producto")
	print("3. comprar un producto")
	print("4. salir")

	op = input("ingrese opcion: ")
	if op == 1:

		url = "http://192.168.0.11:5050"
		response = urllib2.urlopen(url).read()
		data = json.loads(response)

		it = 0
		while(it < len(productos)):
			print "PRODUCTO: "+str(productos[it])+", CANTIDAD: "+data[1][productos[it]]
			it = it+1

	if op == 2:
		
		url = "http://192.168.0.11:5050"
		response = urllib2.urlopen(url).read()
		data = json.loads(response)

		product = raw_input("nombre del producto: ")

		print "INFORMACION DEL PRODUCTO: "+ str(product).upper()
		print "ID ---------------------> "+data[0][product]
		print "CANTIDAD ---------------> "+data[1][product]
		print "PROVEEDOR --------------> "+data[2][product]
		print "FECHA DE VENCIMIENTO ---> "+data[3][product]
		#it = it+1
		
	if op == 3:

		url = "http://192.168.0.11:5050"
		response = urllib2.urlopen(url).read()
		data = json.loads(response)

		product = raw_input("nombre del producto: ")

		if data[1][product] == str(0):
			params = urllib.urlencode({
                  'producto': product,
                  'cantidad': str(200)
                })
			url = 'http://192.168.0.11:5050/actualizar'
			response = urllib2.urlopen(url, params).read()

			url = "http://192.168.0.11:5050"
			response = urllib2.urlopen(url).read()
			data = json.loads(response)

		cantidad = raw_input("cantidad de producto: ")

		#print int(cantidad)
		if int(cantidad) > int(data[1][product]):
			while int(cantidad) > int(data[1][product]):
				print "la cantidad pedida sobrepasa la cantidad actual del inventario : "+data[1][product]
				cantidad = raw_input("vuelve a introducir la cantidad de producto: ")
		
		params = urllib.urlencode({
                  'producto': product,
                  'cantidad': cantidad
                })
		url = 'http://192.168.0.11:5050/comprar'
		response = urllib2.urlopen(url, params).read()
		print "compra realizada con exito"
		#print response

	if op == 4:
		menu = False


pathURL = ''
extension = []
	
	

