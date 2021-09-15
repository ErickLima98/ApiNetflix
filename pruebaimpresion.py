

def creararchivo():
    archivo=open('datos.json', 'w')
    archivo.close()

def escribir():
    archivo=open('datos.json', 'a')
    archivo.write('hola mundo')

creararchivo()
escribir()      