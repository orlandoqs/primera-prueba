import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Aquí indico el servidor (url) y el puerto
mysock.connect(('www.w3.org', 80))

#para solicitar datos con http utilizo el comando get archivo_solicitado url protocolo (http/1.0) salto de linea \r.... la función encode() codifica la estring
cmd = 'GET https://www.w3.org/TR/PNG/iso_8859-1.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

continuar=0
while continuar==0:
# la función recv recibe los datos en grupos de 512 bytes
    data = mysock.recv(512)
if len(data) < 1:
continuar=1
else:
# la función decode() decodifica los datos recibidos
    print(data.decode(),end='')
#cierro la conexión
mysock.close()

El mismos ejemplo utilizando la librería urllib

import urllib.request
# Tabién puedo poner wwww.marca.es
fhand = urllib.request.urlopen('https://www.w3.org/TR/PNG/iso_8859-1.txt')
for line in fhand:
print(line.decode().strip())
