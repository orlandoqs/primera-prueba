import pymysql
from claseconnect import *

clasecon=Claseconnect()

clasecon.EjecutarSql("SELECT * FROM personal")

datos = clasecon.DevolverDatos()

for fila in datos:
    id=fila[0]
    nombre=fila[1]
    apellido=fila[2]
    print(f"El nombre del cliente es {nombre} su id es {id} y su apellido es {apellido}")

clasecon.CerrarBasededatos()