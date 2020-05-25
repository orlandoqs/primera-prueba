import pymysql
from claseconnect import *

clasecon=Claseconnect()

nombre=input("Introduce un nombre: ")
#id=input("Introduce un id: ")

clasecon.EjecutarSql("SELECT * FROM personal WHERE nombre like '"+nombre+"%'")
#clasecon.EjecutarSql("SELECT * FROM personaL WHERE nombre='Jose'")
#clasecon.EjecutarSql("SELECT * FROM personal WHERE id="+id)

datos=clasecon.DevolverDatos()

for fila in datos:
    id=fila[0]
    nombre=fila[1]
    apellido=fila[2]
    print(f"El nombre del cliente es {nombre} su id es {id} y su apellido es {apellido}")

clasecon.CerrarBasededatos()