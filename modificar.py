import pymysql
from claseconnect import *

db=Claseconnect()

identificador=input("Introduce un ID: ")
sql1="SELECT * from personal WHERE ID ="+identificador

db.EjecutarSql(sql1)

resultado=db.DevolverDatos()

if len(resultado) > 0:
    print(resultado)
    nombre=input("Introduce el nombre: ")
    apellido=input("Introduce el apellido: ")
    sql="Update personal set nombre='"+nombre+"', apellido='"+apellido+"' WHERE id="+identificador
    try:
        db.EjecutarSql(sql)
        db.RealizarCambio()
        print("Cambio realizado.")
        db.EjecutarSql(sql1)
        resultado=db.DevolverDatos()
        print(resultado)
    except:
        db.Deshacercambio()
        print("No se puede realizar el cambio.")

else:
    print("Id no valido")

db.CerrarBasededatos()