import pymysql

db = pymysql.connect(
    host="localhost",
    port=3306,
    user="root",
    passwd="",
    db="alumnos",
)
cursor = db.cursor()

cursor.execute("SELECT * FROM personal")

datos=cursor.fetchall()

for fila in datos:
    id=fila[0]
    nombre=fila[1]
    apellido=fila[2]
    print(f"El nombre del cliente es {nombre} su id es {id} y su apellido es {apellido}")

db.close()