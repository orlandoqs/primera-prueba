import pymysql


db = pymysql.connect(
    host="localhost",
    port=3306,
    user="root",
    passwd="",
    db="alumnos",
)
cursor = db.cursor()
cursor.execute("SELECT VERSION()")