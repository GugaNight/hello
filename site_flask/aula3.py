from flask import Flask, redirect, render_template, request, url_for


app = Flask(__name__)

@app.route('/login/', methods=['GET', 'POST'])
def login():
    metodo = request.method
    if metodo == 'POST':
        nome = request.form['nome']
        senha = request.form['senha']
        if nome == 'admin' and senha == 'admin':
            return "oi admin"
        else:
            return "info incorreta"
    else:
        return render_template('login.html')

@app.route('/admin/')
def admin():
    usuario = 'admin'
    return render_template('usuario.html', usuario = usuario)

@app.route('/aluno/')
def aluno():
    usuario = 'Aluno'
    return render_template('usuario.html', usuario = usuario)

@app.route('/professor/')
def admin():
    usuario = 'Professor'
    return render_template('usuario.html', usuario = usuario)

@app.route('/user/<tipo>')
def usuario(tipo):
    if tipo == 'aluno':
        return redirect(url_for('aluno'))
    elif tipo == 'professor':
        return redirect(url_for('professor'))
    elif tipo == 'admin':
        return redirect(url_for('admin'))
    else:
        return '''<h1>user n encontrado</h1>'''

@app.route('/usuarios/')
def lista_usuarios():
    lista_users = ['aluno','professor','admin']
    return render_template('usuarios.html', lista_users = lista_users)

if(__name__ == "__main__"):
    app.run()