from flask import Flask, request, render_template_string

app = Flask(__name__)

usuarios_cadastrados = [
    {"usuario": "aluno", "senha": "suamatricula"},
    {"usuario": "marcos", "senha": "cotemig2026"},
    {"usuario": "janaina", "senha": "cotemig2026"}
]

def show_the_login_form():
    return render_template_string("""
        <div style="text-align: center; margin-top: 50px; font-family: Arial, sans-serif;">
            <h2>Login - Atividade 5</h2>
            <form method="POST">
                <input type="text" name="usuario" placeholder="Usuário" required><br><br>
                <input type="password" name="senha" placeholder="Senha" required><br><br>
                <button type="submit">Entrar</button>
            </form>
        </div>
    """)

def do_the_login():
    usuario_digitado = request.form.get('usuario')
    senha_digitada = request.form.get('senha')

    for credencial in usuarios_cadastrados:
        if credencial['usuario'] == usuario_digitado and credencial['senha'] == senha_digitada:
            return f"<h1 style='color: green; text-align: center;'>Acesso Permitido! Bem-vindo(a), {usuario_digitado}!</h1>"
    
    return """
        <div style="text-align: center; margin-top: 50px; font-family: Arial, sans-serif;">
            <h1 style='color: red;'>Login inválido!</h1>
            <a href="/login">Tentar novamente</a>
        </div>
    """

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return do_the_login()
    else:
        return show_the_login_form()

if __name__ == "__main__":
    app.run(debug=True)