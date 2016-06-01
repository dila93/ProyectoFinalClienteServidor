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

		url = "http://10.253.64.96:5050"
		response = urllib2.urlopen(url).read()
		data = json.loads(response)

		it = 0
		while(it < len(productos)):
			print "PRODUCTO: "+str(productos[it])+", CANTIDAD: "+data[1][productos[it]]
			it = it+1

	if op == 2:
		
		url = "http://10.253.64.96:5050"
		response = urllib2.urlopen(url).read()
		data = json.loads(response)

		product = raw_input("nombre del producto: ")

		if product == 'panela':

			print "INFORMACION DEL PRODUCTO: "+ str(product).upper()
			print "ID ---------------------> "+data[0][product]
			print "CANTIDAD ---------------> "+data[1][product]
			print "PROVEEDOR --------------> "+data[2][product]
			print "FECHA DE VENCIMIENTO ---> "+data[3][product]

		elif product == 'arroz':

			print "INFORMACION DEL PRODUCTO: "+ str(product).upper()
			print "ID ---------------------> "+data[0][product]
			print "CANTIDAD ---------------> "+data[1][product]
			print "PROVEEDOR --------------> "+data[2][product]
			print "FECHA DE VENCIMIENTO ---> "+data[3][product]

		elif product == 'chorizo':

			print "INFORMACION DEL PRODUCTO: "+ str(product).upper()
			print "ID ---------------------> "+data[0][product]
			print "CANTIDAD ---------------> "+data[1][product]
			print "PROVEEDOR --------------> "+data[2][product]
			print "FECHA DE VENCIMIENTO ---> "+data[3][product]

		elif product == 'mantequilla':

			print "INFORMACION DEL PRODUCTO: "+ str(product).upper()
			print "ID ---------------------> "+data[0][product]
			print "CANTIDAD ---------------> "+data[1][product]
			print "PROVEEDOR --------------> "+data[2][product]
			print "FECHA DE VENCIMIENTO ---> "+data[3][product]

		elif product == 'chocolate':

			print "INFORMACION DEL PRODUCTO: "+ str(product).upper()
			print "ID ---------------------> "+data[0][product]
			print "CANTIDAD ---------------> "+data[1][product]
			print "PROVEEDOR --------------> "+data[2][product]
			print "FECHA DE VENCIMIENTO ---> "+data[3][product]

		elif product == 'carne':

			print "INFORMACION DEL PRODUCTO: "+ str(product).upper()
			print "ID ---------------------> "+data[0][product]
			print "CANTIDAD ---------------> "+data[1][product]
			print "PROVEEDOR --------------> "+data[2][product]
			print "FECHA DE VENCIMIENTO ---> "+data[3][product]

		elif product == 'arepas':

			print "INFORMACION DEL PRODUCTO: "+ str(product).upper()
			print "ID ---------------------> "+data[0][product]
			print "CANTIDAD ---------------> "+data[1][product]
			print "PROVEEDOR --------------> "+data[2][product]
			print "FECHA DE VENCIMIENTO ---> "+data[3][product]

		elif product == 'huevos':

			print "INFORMACION DEL PRODUCTO: "+ str(product).upper()
			print "ID ---------------------> "+data[0][product]
			print "CANTIDAD ---------------> "+data[1][product]
			print "PROVEEDOR --------------> "+data[2][product]
			print "FECHA DE VENCIMIENTO ---> "+data[3][product]

		else:
			print "el nombre del producto es invalido"

		#it = it+1
		
	if op == 3:

		url = "http://10.253.64.96:5050"
		response = urllib2.urlopen(url).read()
		data = json.loads(response)

		product = raw_input("nombre del producto: ")

		if product == 'panela':
			if data[1][product] == str(0):
				params = urllib.urlencode({
	                  'producto': product,
	                  'cantidad': str(200)
	                })
				url = 'http://10.253.64.96:5050/actualizar'
				response = urllib2.urlopen(url, params).read()

				url = "http://10.253.64.96:5050"
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
			url = 'http://10.253.64.96:5050/comprar'
			response = urllib2.urlopen(url, params).read()
			print "compra realizada con exito"

		elif product == 'panela':
			if data[1][product] == str(0):
				params = urllib.urlencode({
	                  'producto': product,
	                  'cantidad': str(200)
	                })
				url = 'http://10.253.64.96:5050/actualizar'
				response = urllib2.urlopen(url, params).read()

				url = "http://10.253.64.96:5050"
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
			url = 'http://10.253.64.96:5050/comprar'
			response = urllib2.urlopen(url, params).read()
			print "compra realizada con exito"

		elif product == 'arroz':
			if data[1][product] == str(0):
				params = urllib.urlencode({
	                  'producto': product,
	                  'cantidad': str(200)
	                })
				url = 'http://10.253.64.96:5050/actualizar'
				response = urllib2.urlopen(url, params).read()

				url = "http://10.253.64.96:5050"
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
			url = 'http://10.253.64.96:5050/comprar'
			response = urllib2.urlopen(url, params).read()
			print "compra realizada con exito"

		elif product == 'chorizo':
			if data[1][product] == str(0):
				params = urllib.urlencode({
	                  'producto': product,
	                  'cantidad': str(200)
	                })
				url = 'http://10.253.64.96:5050/actualizar'
				response = urllib2.urlopen(url, params).read()

				url = "http://10.253.64.96:5050"
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
			url = 'http://10.253.64.96:5050/comprar'
			response = urllib2.urlopen(url, params).read()
			print "compra realizada con exito"

		elif product == 'mantequilla':
			if data[1][product] == str(0):
				params = urllib.urlencode({
	                  'producto': product,
	                  'cantidad': str(200)
	                })
				url = 'http://10.253.64.96:5050/actualizar'
				response = urllib2.urlopen(url, params).read()

				url = "http://10.253.64.96:5050"
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
			url = 'http://10.253.64.96:5050/comprar'
			response = urllib2.urlopen(url, params).read()
			print "compra realizada con exito"

		elif product == 'chocolate':
			if data[1][product] == str(0):
				params = urllib.urlencode({
	                  'producto': product,
	                  'cantidad': str(200)
	                })
				url = 'http://10.253.64.96:5050/actualizar'
				response = urllib2.urlopen(url, params).read()

				url = "http://10.253.64.96:5050"
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
			url = 'http://10.253.64.96:5050/comprar'
			response = urllib2.urlopen(url, params).read()
			print "compra realizada con exito"
		#print response

		elif product == 'carne':
			if data[1][product] == str(0):
				params = urllib.urlencode({
	                  'producto': product,
	                  'cantidad': str(200)
	                })
				url = 'http://10.253.64.96:5050/actualizar'
				response = urllib2.urlopen(url, params).read()

				url = "http://10.253.64.96:5050"
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
			url = 'http://10.253.64.96:5050/comprar'
			response = urllib2.urlopen(url, params).read()
			print "compra realizada con exito"

		elif product == 'arepas':
			if data[1][product] == str(0):
				params = urllib.urlencode({
	                  'producto': product,
	                  'cantidad': str(200)
	                })
				url = 'http://10.253.64.96:5050/actualizar'
				response = urllib2.urlopen(url, params).read()

				url = "http://10.253.64.96:5050"
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
			url = 'http://10.253.64.96:5050/comprar'
			response = urllib2.urlopen(url, params).read()
			print "compra realizada con exito"

		elif product == 'huevos':
			if data[1][product] == str(0):
				params = urllib.urlencode({
	                  'producto': product,
	                  'cantidad': str(200)
	                })
				url = 'http://10.253.64.96:5050/actualizar'
				response = urllib2.urlopen(url, params).read()

				url = "http://10.253.64.96:5050"
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
			url = 'http://10.253.64.96:5050/comprar'
			response = urllib2.urlopen(url, params).read()
			print "compra realizada con exito"

		else:
			print "nombre del producto es invalido"

	if op == 4:
		menu = False


pathURL = ''
extension = []
	
	

