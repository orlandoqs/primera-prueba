import pymysql
from claseconnect import *

clasecon=Claseconnect()

nombre=input("Introduce un nombre: ")
apellido=input("Introduce un apellido: ")

clasecon.EjecutarSql("INSERT INTO personal (nombre,apellido) VALUES ('"+nombre+"','"+apellido+"')")

clasecon.RealizarCambio()

datos=clasecon.DevolverDatos()

clasecon.CerrarBasededatos()