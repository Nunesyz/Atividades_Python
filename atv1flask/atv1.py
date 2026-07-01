from flask import Flask


app = Flask(__name__) # inicio o flask

@app.route('/decorator') # Isso é o decorator, ele é usado para mapear a função abaixo para a rota '/'
def conceito():
    return '1- O que é um decorator em Python? \nR: São funções que modificam ou aprimoram o comportamento de outras funções ou métodos sem alterar seu código-fonte original'

if __name__ == '__main__':
    app.run(debug=True) # Isso inicia o servidor Flask em modo de depuração, o que é útil para desenvolvimento