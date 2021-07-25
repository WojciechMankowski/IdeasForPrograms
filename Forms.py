from wtforms import Form, StringField, TextAreaField, SelectField, IntegerField
from flask_wtf import FlaskForm
class Forms(Form):
    choices_lidt = [
        'Zarys projekty', "Część napisana", "Projekt na Githubie", "Testy programu", "Zakończony"
    ]
    name_project = StringField("Nazwa projektu")
    status = SelectField("Status projektu", choices=choices_lidt)
    link = StringField("Link do Githubu")
    opis = TextAreaField("Opis projektu")
    rating = IntegerField("Ocena projektu od 0 do 10")