from wtforms import Form, StringField, TextAreaField, SelectField, IntegerField
from wtforms.validators import NumberRange, Optional, URL
from APINote import NotionAPISupport
class Forms(Form):
    choices_lidt = ["",
        'Zarys projekty', "Część napisana", "Projekt na Githubie", "Testy programu", "Zakończony"
    ]
    name_project = StringField("Nazwa projektu: ")
    status = SelectField("Status projektu: ", choices=choices_lidt)
    link = StringField("Link do Githubu: ", [Optional(strip_whitespace =True), URL(message="Nie poprawny adres URL")])
    opis = TextAreaField("Opis projektu: ")
    rating = IntegerField("Ocena projektu od 0 do 10: ", [NumberRange(min=0, max=10,
                                                                     message="Nie odpowiednia liczba została wpisana")] )

def chacking(name_project, status, link, opis, rating):
    if name_project != "" and status != "":
        if not 'localhost' in link:
            if rating >= 0 and rating <= 10:
                return True
    return False
class OpinionsForms(Form):
    choices_list = NotionAPISupport().DowlandTitle()
    print(type(choices_list))
    if type(choices_list) == "NoneType":
        choices_list: [""]
    title = SelectField('Wybierz pomysł: ', choices=choices_list)
    rating = IntegerField("Ocena projektu od 0 do 10: ", [NumberRange(min=0, max=10, message="Nie odpowiednia liczba została wpisana")] )
    comment = StringField('Komentarz do pomysłu: ')