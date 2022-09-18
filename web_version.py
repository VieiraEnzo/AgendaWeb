from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html")


@app.route("/inserir")
def inserirfunc():
    return render_template("inserir.html")


@app.route("/deletar")
def deletarfunc():
    return render_template("deletar.html")


@app.route("/buscar")
def buscarfunc():
    return render_template("buscar.html")


@app.route("/erro")
def errofunc():
    return render_template("erro.html")


app.run()