from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    nome = "Ana"
    idade = 18

    usuario = {
        "nome": "Ana",
        "email": "ana@email.com"
    }

    alunos = ["João", "Maria", "Pedro"]

    nota = 8

    return render_template(
        "index.html",
        nome=nome,
        idade=idade,
        usuario=usuario,
        alunos=alunos,
        nota=nota
    )

app.run(debug=True)