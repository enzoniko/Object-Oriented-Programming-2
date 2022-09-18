from copyreg import remove_extension
from flask_wtf import FlaskForm
from wtforms import SubmitField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Length


class AdminLoginForm(FlaskForm):
    password = PasswordField('Password', validators=[
                             DataRequired(), Length(min=8, max=20)])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Login')
