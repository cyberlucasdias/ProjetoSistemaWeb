from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3
import os
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'secreto'  # chave para mensagens flash

DATABASE = 'refeicoes.db'

#Função para conectar ao banco
def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

#Inicializa o banco e cria a tabela se não existir
def init_db():
    if not os.path.exists(DATABASE):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE refeicoes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                data TEXT NOT NULL,
                tipo TEXT NOT NULL,
                descricao TEXT NOT NULL
            )
        ''')
        conn.commit()
        conn.close()
        print("Banco de dados e tabela 'refeicoes' criados.")

#Rota a tela principal exibindo as refeições do dia atual com opção de adicionar mais uma
@app.route('/admin')
def index():
    hoje = datetime.now().strftime('%Y-%m-%d')
    conn = get_db_connection()
    refeicoes = conn.execute('SELECT * FROM refeicoes WHERE data = ?', (hoje,)).fetchall()
    conn.close()
    return render_template('index.html', refeicoes=refeicoes, hoje=hoje)

#Rota para adicionar uma nova refeição
@app.route('/adicionar', methods=['GET', 'POST'])
def adicionar():
    if request.method == 'POST':
        data = request.form['data']
        tipo = request.form['tipo']
        descricao = request.form['descricao']

        conn = get_db_connection()
        conn.execute('INSERT INTO refeicoes (data, tipo, descricao) VALUES (?, ?, ?)',
                     (data, tipo, descricao))
        conn.commit()
        conn.close()
        flash('Refeição adicionada com sucesso!')
        return redirect(url_for('index'))

    return render_template('adicionar.html')

#Rota para editar uma refeição
@app.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    if request.method == 'POST':
        data = request.form['data']
        tipo = request.form['tipo']
        descricao = request.form['descricao']
        cursor.execute('UPDATE refeicoes SET data = ?, tipo = ?, descricao = ? WHERE id = ?', (data, tipo, descricao, id))
        conn.commit()
        conn.close()
        flash('Refeição atualizada com sucesso!')
        return redirect(url_for('index'))

    cursor.execute('SELECT * FROM refeicoes WHERE id = ?', (id,))
    refeicao = cursor.fetchone()
    conn.close()

    if refeicao is None:
        flash('Refeição não encontrada.')
        return redirect(url_for('index'))

    return render_template('editar.html', refeicao=refeicao)

#Função para excluir refeição
@app.route('/excluir/<int:id>', methods=['POST'])
def excluir(id):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('DELETE FROM refeicoes WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    flash('Refeição excluída com sucesso!')
    return redirect(url_for('index'))

#Rota pública: exibe as refeições do dia atual sem botões de edição ou exclusão
@app.route('/')
def publico():
    conn = get_db_connection()
    hoje = datetime.now().strftime('%Y-%m-%d')
    refeicoes = conn.execute('SELECT * FROM refeicoes WHERE data = ?', (hoje,)).fetchall()
    conn.close()

    return render_template('publico.html', refeicoes=refeicoes, hoje=hoje)

#Rota para logout (se for necessário)
@app.route('/logout')
def logout():
    # Exemplo simples de logout, pode ser alterado conforme necessidade
    flash("Você saiu da tela pública.")
    return redirect(url_for('index'))  # Ou redirecionar para qualquer outra página.

if __name__ == '__main__':
    init_db()
    app.run(debug=True)

application = app