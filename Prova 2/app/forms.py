from datetime import datetime, timedelta
from flask_wtf import FlaskForm
from wtforms import SubmitField, PasswordField, BooleanField, IntegerField, SelectField, StringField, FieldList, DateField
from wtforms.validators import DataRequired, Length, NumberRange

class LoginForm(FlaskForm):
    login = StringField('Username', validators=[DataRequired(), Length(min=4, max=20)])
    senha = PasswordField('Password', validators=[DataRequired(), Length(min=8, max=20)])
    submit = SubmitField('Login')

class RegisterForm(FlaskForm):
    nome = StringField('Nome', validators=[DataRequired(), Length(min=4, max=20)])
    sobrenome = StringField('Sobrenome', validators=[DataRequired(), Length(min=4, max=20)])
    idade = IntegerField('Idade', validators=[DataRequired(), NumberRange(min=0, max=120)])
    genero = SelectField('Genero', choices=[('Masculino', 'Masculino'), ('Femenino', 'Femenino')])
    cpf = StringField('CPF', validators=[DataRequired(), Length(min=11, max=11)])
    email = StringField('Email', validators=[DataRequired(), Length(min=4, max=20)])
    login = StringField('Login', validators=[DataRequired(), Length(min=4, max=20)])
    senha = PasswordField('Password', validators=[DataRequired(), Length(min=8, max=20)])
    telefone = StringField('Telefone', validators=[DataRequired(), Length(min=4, max=20)])
    endereco = StringField('Endereco', validators=[DataRequired(), Length(min=4, max=20)])
    submit = SubmitField('Register')

class FilterNewsForm(FlaskForm):
    DataInicio = DateField('DataInicio', validators=[DataRequired()], default=datetime.now() - timedelta(days=30))
    DataFim = DateField('DataFim', validators=[DataRequired()], default=datetime.now())
    assunto = StringField('Assunto', validators=[DataRequired()])
    categoria = SelectField('Categoria', choices=[('business', 'Negócios'), ('entertainment', 'Entretenimento'), ('general', 'Geral'), ('health', 'Saúde'), ('science', 'Ciência'), ('sports', 'Esportes'), ('technology', 'Tecnologia')])
    filtrarPor = SelectField('FiltrarPor', choices=[('relevancy', 'Relevância'), ('popularity', 'Popularidade'), ('publishedAt', 'Cronologicamente')])
    submit = SubmitField('Filtrar')