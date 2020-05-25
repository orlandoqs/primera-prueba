import pymysql

class Claseconnect():
    def __init__(self):
        #conectarme con la base de datos
        #abrir la conexion
        self.CrearConect()
        self.AbrirConnect()

    def CrearConect(self):
        self.db = pymysql.connect(
            host="localhost",
            port=3306,
            user="root",
            passwd="",
            db="alumnos",
        )

    def AbrirConnect(self):
        self.cursor = self.db.cursor()

    def EjecutarSql(self,sql):
        self.cursor.execute(sql)

    def DevolverDatos(self):
        return self.cursor.fetchall()
        
    def CerrarBasededatos(self):
        self.db.close()

    def RealizarCambio(self):
        self.db.commit()

    def Deshacercambio(self):
        self.db.rollback()
    