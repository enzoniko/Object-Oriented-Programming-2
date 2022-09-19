from flask import render_template, flash, redirect, url_for, request
from app import app
from app.forms import AdminLoginForm, CompraForm
# Need a function that gets stuff from the database and puts it in
# a good format to be used by our backend in sessoes list and pagamentos list etc
from app.models import Session, Payment
from app.Backend.main import sessoes, filmes, pagamentos, printar_filmes, printar_sessoes, sala_mais_vazia
from app.Backend.helpers import most_empty
from app.Backend.sala import salas
quantidade_lugares_disponiveis_sala_mais_vazia = 0

@app.route('/', methods=['GET', 'POST'])
def escolha_do_filme():
    sessions = {}
    for sessao in sessoes:
        if sessao.get_nome() not in sessions:
           
            sessions[sessao.get_nome()] = []

            for each in [s for s in sessoes if s.get_nome() == sessao.get_nome()]:
                new = [each.get_generos(), each.get_legenda(), each.get_DDD(), each.get_horarios(), each.get_id()]
                sessions[sessao.get_nome()].append(new)

    return render_template('escolha_do_filme.html', title='Filmes', filmes=printar_filmes(), sessions=sessions, sessoes=sessoes)

@app.route('/poltronas/<id_sessao>/<horario>', methods=['GET', 'POST'])
def poltronas(id_sessao, horario):
    session = [sessao for sessao in sessoes if sessao.get_id() == id_sessao][0]
    quantidade_lugares_disponiveis_sala_mais_vazia = most_empty(
        [
            [
                sala.get_cronograma()[
                    f"{id_sessao} {horario}"
                ]
                for sessao in sala.get_sessoes()
                if sessao.get_id() == id_sessao
            ]
            for sala in salas
        ]
    )
    sala = sala_mais_vazia(quantidade_lugares_disponiveis_sala_mais_vazia, session)
    poltronas = sala.get_cronograma()[f"{id_sessao} {horario}"]
    sala.preencher_poltronas(["b10", "b9"], id_sessao, horario)
    sala.printar_poltronas(id_sessao, horario)
    print(request.form)
    ingressos = request.form.getlist('poltronas')
    print("lista: ", ingressos)
    form = CompraForm()
    if form.validate_on_submit():
        
        if form.meias.data > len(ingressos):
            flash('Você não pode comprar mais meias-entradas do que ingressos. Por favor, escolha um número menor de meias-entradas.')
        else:
            flash(f'Você comprou {len(ingressos)} ingressos e {form.meias.data} meias-entradas.')
            return redirect(url_for('escolha_do_filme'))
    return render_template('poltronas.html', title='Sessoes', horario = horario, sessao = session, form=form, poltronas=poltronas)


@app.route('/adminLogin', methods=['GET', 'POST'])
def adminLogin():
    form = AdminLoginForm()
    if form.validate_on_submit():
        if form.password.data == "adminadmin":
            # flash(" ", "class")
            flash("Admin logged in successfully!")
            return redirect(url_for('home'))
        else:
            flash("Login unsuccessful. Please check username and password")
    return render_template('adminLogin.html', title="Admin Login", form=form)
