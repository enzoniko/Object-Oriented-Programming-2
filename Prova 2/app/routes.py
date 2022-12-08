# Imports
from datetime import datetime, timedelta
from typing import Dict, List
from flask import render_template, redirect, url_for, request
from app import app
from app.forms import FilterNewsForm, LoginForm, RegisterForm
from app.Backend.api import get_all_articles
from app.Backend.usuario import Usuario
from app.Backend.helpers import *

# Se os arquivos estiverem vazios guarda novos objetos (pra iniciar com algo), se tiver objetos para serem lidos, carrega
usuarios: List[Usuario] = list(load_objects('app/storage/usuarios.pkl')) or store_objects([
        Usuario("João", "Silva", 20, "Masculino", "123.456.789-00", "joao", "12341234", "email", "telefone", "endereco"), 
        Usuario("Maria", "Silva", 20, "Femenino", "123.456.689-00", "maria", "12341234", "email", "telefone", "endereco")
    ], "app/storage/usuarios.pkl")

@app.route('/', methods=['GET', 'POST'])
def register():
    form: RegisterForm = RegisterForm()
    if form.validate_on_submit():
        new_user = Usuario(form.nome.data, form.sobrenome.data, form.idade.data, form.genero.data, form.cpf.data, form.login.data, form.senha.data, form.email.data, form.telefone.data, form.endereco.data)
        if new_user not in usuarios:
            usuarios.append(new_user)
            store_objects(usuarios, "app/storage/usuarios.pkl")
            return redirect(url_for('login'))
    return render_template('register.html', title = "Register", form = form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form: LoginForm = LoginForm()
    if form.validate_on_submit():
        for user in usuarios:
            if user.login == form.login.data and user.senha == form.senha.data:
                return redirect(url_for('main', user_id = usuarios.index(user), q = 'futbol', category = 'sports', sort_by = 'publishedAt', data_inicio = (datetime.now() - timedelta(days=30)).strftime("%Y-%m-%d"), data_fim = datetime.now().strftime("%Y-%m-%d")))
    return render_template('login.html', title = "Login", form = form)

@app.route('/main/<user_id>/<q>/<category>/<sort_by>/<data_inicio>/<data_fim>', methods=['GET', 'POST'])
def main(user_id: str, q: str = 'futbol', category: str = 'sports', sort_by: str = 'publishedAt', data_inicio: str = (datetime.now() - timedelta(days=30)).strftime("%Y-%m-%d"), data_fim: str = datetime.now().strftime("%Y-%m-%d")):
    form: FilterNewsForm = FilterNewsForm()
    if form.validate_on_submit():
     
        return redirect(url_for('main', user_id = user_id, q = form.assunto.data, category = form.categoria.data, sort_by = form.filtrarPor.data, data_inicio = form.DataInicio.data, data_fim = form.DataFim.data))
    return render_template('main.html', form=form, title = "Main", user = usuarios[int(user_id)], articles = get_all_articles(q = q, category = category, sort_by = sort_by, from_param=data_inicio, to=data_fim))