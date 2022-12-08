from datetime import datetime
from flask_wtf import FlaskForm
from wtforms import SubmitField, PasswordField, BooleanField, IntegerField, SelectField, StringField, FieldList, TimeField
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

