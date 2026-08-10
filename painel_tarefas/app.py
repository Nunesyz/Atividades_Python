from flask import Flask, render_template, request, redirect, url_for, session, flash, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps
import sqlite3
import requests

app = Flask(__name__)
app.config['SECRET_KEY'] = 'chave-secreta-painel-tarefas'
app.config['DEBUG'] = False


def obter_conexao():
    conexao = sqlite3.connect('banco.db')
    conexao.row_factory = sqlite3.Row
    return conexao


def inicializar_bd():
    conexao = obter_conexao()
    conexao.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            senha TEXT NOT NULL
        )
    ''')
    conexao.execute('''
        CREATE TABLE IF NOT EXISTS tarefas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            descricao TEXT,
            status TEXT NOT NULL DEFAULT 'Pendente',
            usuario_id INTEGER NOT NULL,
            FOREIGN KEY (usuario_id) REFERENCES usuarios (id)
        )
    ''')
    conexao.commit()
    conexao.close()


def login_obrigatorio(funcao):
    @wraps(funcao)
    def decorada(*args, **kwargs):
        if 'usuario_id' not in session:
            return redirect(url_for('login'))
        return funcao(*args, **kwargs)
    return decorada


@app.route('/')
def index():
    if 'usuario_id' in session:
        return redirect(url_for('dashboard'))
    return redirect(url_for('login'))


@app.route('/registro', methods=['GET', 'POST'])
def registro():
    if request.method == 'POST':
        nome = request.form.get('nome', '').strip()
        email = request.form.get('email', '').strip()
        senha = request.form.get('senha', '').strip()

        if not nome or not email or not senha:
            flash('Preencha todos os campos')
            return redirect(url_for('registro'))

        senha_hash = generate_password_hash(senha)
        conexao = obter_conexao()
        try:
            conexao.execute('INSERT INTO usuarios (nome, email, senha) VALUES (?, ?, ?)', (nome, email, senha_hash))
            conexao.commit()
        except sqlite3.IntegrityError:
            flash('Este email já está cadastrado')
            conexao.close()
            return redirect(url_for('registro'))
        conexao.close()
        return redirect(url_for('login'))
    return render_template('registro.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email', '').strip()
        senha = request.form.get('senha', '').strip()

        conexao = obter_conexao()
        usuario = conexao.execute('SELECT * FROM usuarios WHERE email = ?', (email,)).fetchone()
        conexao.close()

        if usuario and check_password_hash(usuario['senha'], senha):
            session['usuario_id'] = usuario['id']
            session['usuario_nome'] = usuario['nome']
            return redirect(url_for('dashboard'))

        flash('Email ou senha incorretos')
        return redirect(url_for('login'))
    return render_template('login.html')


@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))


@app.route('/dashboard')
@login_obrigatorio
def dashboard():
    conexao = obter_conexao()
    tarefas = conexao.execute('SELECT * FROM tarefas WHERE usuario_id = ?', (session['usuario_id'],)).fetchall()
    conexao.close()

    frase = 'Não foi possível carregar a frase do dia'
    try:
        resposta = requests.get('https://api.adviceslip.com/advice', timeout=5)
        frase = resposta.json()['slip']['advice']
    except Exception:
        pass

    return render_template('dashboard.html', tarefas=tarefas, frase=frase)


@app.route('/nova_tarefa', methods=['GET', 'POST'])
@login_obrigatorio
def nova_tarefa():
    if request.method == 'POST':
        titulo = request.form.get('titulo', '').strip()
        descricao = request.form.get('descricao', '').strip()
        status = request.form.get('status', 'Pendente')

        if not titulo:
            flash('O título é obrigatório')
            return redirect(url_for('nova_tarefa'))

        conexao = obter_conexao()
        conexao.execute('INSERT INTO tarefas (titulo, descricao, status, usuario_id) VALUES (?, ?, ?, ?)',
                         (titulo, descricao, status, session['usuario_id']))
        conexao.commit()
        conexao.close()
        return redirect(url_for('dashboard'))
    return render_template('nova_tarefa.html')


@app.route('/editar/<int:id>', methods=['GET', 'POST'])
@login_obrigatorio
def editar(id):
    conexao = obter_conexao()
    tarefa = conexao.execute('SELECT * FROM tarefas WHERE id = ? AND usuario_id = ?', (id, session['usuario_id'])).fetchone()

    if tarefa is None:
        conexao.close()
        return redirect(url_for('dashboard'))

    if request.method == 'POST':
        titulo = request.form.get('titulo', '').strip()
        descricao = request.form.get('descricao', '').strip()
        status = request.form.get('status', 'Pendente')

        if not titulo:
            flash('O título é obrigatório')
            conexao.close()
            return redirect(url_for('editar', id=id))

        conexao.execute('UPDATE tarefas SET titulo = ?, descricao = ?, status = ? WHERE id = ?',
                         (titulo, descricao, status, id))
        conexao.commit()
        conexao.close()
        return redirect(url_for('dashboard'))

    conexao.close()
    return render_template('editar_tarefa.html', tarefa=tarefa)


@app.route('/excluir/<int:id>')
@login_obrigatorio
def excluir(id):
    conexao = obter_conexao()
    conexao.execute('DELETE FROM tarefas WHERE id = ? AND usuario_id = ?', (id, session['usuario_id']))
    conexao.commit()
    conexao.close()
    return redirect(url_for('dashboard'))


@app.route('/concluir/<int:id>')
@login_obrigatorio
def concluir(id):
    conexao = obter_conexao()
    conexao.execute('UPDATE tarefas SET status = ? WHERE id = ? AND usuario_id = ?', ('Concluída', id, session['usuario_id']))
    conexao.commit()
    conexao.close()
    return redirect(url_for('dashboard'))


@app.route('/progresso')
@login_obrigatorio
def progresso():
    return render_template('progresso.html')


@app.route('/api/progresso')
@login_obrigatorio
def api_progresso():
    conexao = obter_conexao()
    pendente = conexao.execute('SELECT COUNT(*) FROM tarefas WHERE usuario_id = ? AND status = ?', (session['usuario_id'], 'Pendente')).fetchone()[0]
    andamento = conexao.execute('SELECT COUNT(*) FROM tarefas WHERE usuario_id = ? AND status = ?', (session['usuario_id'], 'Em andamento')).fetchone()[0]
    concluida = conexao.execute('SELECT COUNT(*) FROM tarefas WHERE usuario_id = ? AND status = ?', (session['usuario_id'], 'Concluída')).fetchone()[0]
    conexao.close()

    return jsonify({'pendente': pendente, 'andamento': andamento, 'concluida': concluida})


@app.route('/api/tarefas', methods=['GET'])
@login_obrigatorio
def api_listar_tarefas():
    status = request.args.get('status')
    conexao = obter_conexao()
    if status:
        tarefas = conexao.execute('SELECT * FROM tarefas WHERE usuario_id = ? AND status = ?', (session['usuario_id'], status)).fetchall()
    else:
        tarefas = conexao.execute('SELECT * FROM tarefas WHERE usuario_id = ?', (session['usuario_id'],)).fetchall()
    conexao.close()
    return jsonify([dict(tarefa) for tarefa in tarefas])


@app.route('/api/tarefas', methods=['POST'])
@login_obrigatorio
def api_criar_tarefa():
    dados = request.get_json(silent=True) or {}
    titulo = dados.get('titulo', '').strip()
    descricao = dados.get('descricao', '')
    status = dados.get('status', 'Pendente')

    if not titulo:
        return jsonify({'erro': 'O título é obrigatório'}), 400

    conexao = obter_conexao()
    cursor = conexao.execute('INSERT INTO tarefas (titulo, descricao, status, usuario_id) VALUES (?, ?, ?, ?)',
                              (titulo, descricao, status, session['usuario_id']))
    conexao.commit()
    id_criado = cursor.lastrowid
    conexao.close()
    return jsonify({'id': id_criado, 'titulo': titulo, 'descricao': descricao, 'status': status}), 201


@app.route('/api/tarefas/<int:id>', methods=['GET'])
@login_obrigatorio
def api_obter_tarefa(id):
    conexao = obter_conexao()
    tarefa = conexao.execute('SELECT * FROM tarefas WHERE id = ? AND usuario_id = ?', (id, session['usuario_id'])).fetchone()
    conexao.close()

    if tarefa is None:
        return jsonify({'erro': 'Tarefa não encontrada'}), 404
    return jsonify(dict(tarefa))


@app.route('/api/tarefas/<int:id>', methods=['PUT'])
@login_obrigatorio
def api_atualizar_tarefa(id):
    conexao = obter_conexao()
    tarefa = conexao.execute('SELECT * FROM tarefas WHERE id = ? AND usuario_id = ?', (id, session['usuario_id'])).fetchone()

    if tarefa is None:
        conexao.close()
        return jsonify({'erro': 'Tarefa não encontrada'}), 404

    dados = request.get_json(silent=True) or {}
    titulo = dados.get('titulo', tarefa['titulo'])
    descricao = dados.get('descricao', tarefa['descricao'])
    status = dados.get('status', tarefa['status'])

    conexao.execute('UPDATE tarefas SET titulo = ?, descricao = ?, status = ? WHERE id = ?', (titulo, descricao, status, id))
    conexao.commit()
    conexao.close()
    return jsonify({'id': id, 'titulo': titulo, 'descricao': descricao, 'status': status})


@app.route('/api/tarefas/<int:id>', methods=['DELETE'])
@login_obrigatorio
def api_excluir_tarefa(id):
    conexao = obter_conexao()
    tarefa = conexao.execute('SELECT * FROM tarefas WHERE id = ? AND usuario_id = ?', (id, session['usuario_id'])).fetchone()

    if tarefa is None:
        conexao.close()
        return jsonify({'erro': 'Tarefa não encontrada'}), 404

    conexao.execute('DELETE FROM tarefas WHERE id = ?', (id,))
    conexao.commit()
    conexao.close()
    return jsonify({'mensagem': 'Tarefa excluída com sucesso'})


if __name__ == '__main__':
    inicializar_bd()
    app.run(debug=False)
