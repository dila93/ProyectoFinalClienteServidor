from BaseHTTPServer import  BaseHTTPRequestHandler, HTTPServer
import mimetypes
import glob
import os
import sys
import json
import cgi

productosyCantidades = {}
stocklist = []
listaIndividual = []
productoss = []
	
productsIDS = {}
	#productsNames = []
productsCantidades = {}
productsProveedores = {}
productsFechasDeVenc = {}

def open_list():
	fr = open("stockBodega.txt","r+")

	while(1):
			
		linea = fr.readline()
		if not linea: break
		productN = linea.split(', ')
		stocklist.append(productN)
			
		productsIDS[productN[1]] = productN[0]
		#productsNames.append(productN[1])
		productsCantidades[productN[1]] = productN[2]
		productsProveedores[productN[1]] = productN[3]
		productsFechasDeVenc[productN[1]] = productN[4].rstrip('\n')
			
		#print stocklist
			
		#print "\n IDS: "+str(productsIDS)
		#print "\n CANTIDADES: "+str(productsCantidades)
		#print "\n PROVEEDORES: "+str(productsProveedores)
		#print "\n FECHAS DE VENC: "+str(productsFechasDeVenc)
			
	fr.close()

open_list()

class http_server:
    def __init__(self):
        server = HTTPServer(('192.168.0.11', 6060), myHandler)
        server.serve_forever()
        
class myHandler(BaseHTTPRequestHandler):
	
		
	def inicializate(self, appPath, path, mimetype):
		self.send_header('Content-type',mimetype)
		self.end_headers()
		
		#~ g = open(appPath + self.path, "rb")
		#~ self.wfile.write(g.read())
		#~ g.close() 

	def do_POST(self):
		global productsCantidades

		if self.path=="/bodega":
			newCantidad = 0
			form = cgi.FieldStorage(
				fp=self.rfile, 
				headers=self.headers,
				environ={'REQUEST_METHOD':'POST',
		                 'CONTENT_TYPE':self.headers['Content-Type'],
			})
			producto = form['producto'].value
			cantidad = form["cantidad"].value
			newCantidad = int(productsCantidades[producto]) - int(cantidad)
			productsCantidades[producto] = str(newCantidad)
			print "la cantidad actual de "+producto+" en la bodega es: "+productsCantidades[producto]
			self.wfile.write("works")

class main:
    def __init__(self):
 
        self.server = http_server()
 
if __name__ == '__main__':
    m = main()

