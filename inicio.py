from flask import Flask

app = Flask(__name__)

print("Hola")

@app.route("/")
def hello():
    return "Hola Don Pepito!"

@app.route("/saludo")
def saludo():
    return "Soy Pepe Gotera"

@app.route("/edit")
def responder():
    return "Orlando"


if __name__ == "__main__":
    app.run()