from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("main.html")


@app.route("/inserir")
def hello_world():
    return render_template("inserir.html")


@app.route("/deletar")
def hello_world():
    return render_template("deletar.html")


@app.route("/buscar")
def hello_world():
    return render_template("buscar.html")


@app.route("/erro")
def hello_world():
    return render_template("erro.html")


app.run()