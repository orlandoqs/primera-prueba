from flask import Flask,jsonify,render_template, request, redirect
from claseconnect import *
import pymysql

app = Flask(__name__)

@app.route("/")
def presentacion():
    return "Bienvenido a mi web."

@app.route("/<name>")
def saludo(name):
    return "Hola Don/Doña " + str(name)
    
@app.route("/add",methods=["POST"])
def insertar():
    try:
        nombre=request.form.get("nombre")
        apellido=request.form.get("apellido")
        conect=Claseconnect()
        conect.EjecutarSql("INSERT INTO personal (nombre,apellido) VALUES('"+nombre+"','"+apellido+"')")
        datos=conect.DevolverDatos()
        conect.RealizarCambio()
        print(datos)
    except Exception:
        conect.Deshacercambio()
        print("Error en las altas")
    return redirect("/all")
    
@app.route("/update" ,methods=["POST"])
def update():
    id=request.form.get("id")
    nombre=request.form.get("nombre")
    apellido=request.form.get("apellido")
    conect=Claseconnect()
    conect.EjecutarSql("UPDATE personal SET nombre='"+nombre+"',apellido='"+apellido+"' WHERE id="+id)
    conect.RealizarCambio()
    return redirect("/all")

@app.route("/delete",methods=["POST"])
def delete():
    try:
        id=request.form.get("id")
        conect=Claseconnect()
        conect.EjecutarSql("DELETE FROM personal WHERE id="+id)
        conect.RealizarCambio()
    except Exception:
        conect.Deshacercambio()
        print("Error en las bajas")
    return redirect("/all")

@app.route("/list")
def listadoalumno():
    connect=Claseconnect()
    connect.EjecutarSql("SELECT * from personal")
    datos=connect.DevolverDatos()
    resp=jsonify(datos)
    connect.CerrarBasededatos()
    return resp

@app.route("/all")
def listall():
    connect=Claseconnect()
    connect.EjecutarSql("SELECT * from personal")
    data=connect.DevolverDatos()
    connect.CerrarBasededatos()
    return render_template("index.html",datos=data)

if __name__ == "__main__":
    #app.run(debug=True, host='0.0.0.0', port=8000)
    app.run()