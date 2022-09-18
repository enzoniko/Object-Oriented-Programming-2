from flask import Flask, render_template, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from forms import AdminLoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'l8G5zgBO2OvULPfkeIwyPFSOGxTH48vv'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

# Need a function that gets stuff from the database and puts it in
# a good format to be used by our backend in sessoes list and pagamentos list etc


class Session(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    # Generos vai ter que ser uma string grande com cada genero separado por virgula
    generos = db.Column(db.String(120), nullable=False)
    legendado = db.Column(db.Boolean, nullable=False)
    # Horarios vai ter que ser uma string grande com cada horario separado por virgula
    horarios = db.Column(db.String(120), nullable=False)
    threeDimensions = db.Column(db.Boolean, nullable=False)

    def __repr__(self):
        return f"User('{self.nome}', '{self.generos}', '{self.legendado}', '{self.horarios}', '{self.threeDimensions}')"


class Payments(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    valor = db.Column(db.Float, nullable=False)
    forma = db.Column(db.String(20), nullable=False)
    ingressos = db.Column(db.Integer, nullable=False)
    meias = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"User('{self.valor}', '{self.forma}', '{self.ingressos}', '{self.meias}')"


@app.route('/')
def home():
    return render_template('home.html', lista=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10])


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


if __name__ == '__main__':
    app.run(debug=True)
