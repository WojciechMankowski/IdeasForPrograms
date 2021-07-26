from flask import Flask, render_template, request
from test import NotionAPISupport
from Forms import Forms, OpinionsForms

app = Flask(__name__)
api = NotionAPISupport()

@app.route("/")
def home():
    resultat = api.GetInformation()
    return resultat

@app.route('/add', methods=['Get', 'POST'])
def addItems():
    form = Forms()
    Form = request.form
    if request.method == "POST":
        name_project = Form.getlist('name_project')[0]
        status = Form.getlist('status')[0]
        link = Form.getlist('link')[0]
        opis = Form.getlist('opis')[0]
        rating = int(Form.getlist('rating')[0])
    return render_template('test.html', form=form)

@app.route('/opinions', methods=['Get', 'POST'])
def opinions():
    form = OpinionsForms()
    return render_template('opinions.html', form=form)
if __name__ == '__main__':
    app.run(debug=True)