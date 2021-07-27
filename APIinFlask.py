from flask import Flask, render_template, request
from APINote import NotionAPISupport
from Forms import Forms, OpinionsForms, chacking

app = Flask(__name__)
api = NotionAPISupport()

@app.route("/")
def home():
    resultat = api.GetInformation()
    listaidea = api.DowlandTitle()
    for item in listaidea:
        one_item = resultat[item]
    lenght = len(resultat)
    return render_template('index.html', ideas=resultat, lista=listaidea)
    # return resultat

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
        CHACKING = chacking(name_project, status, link, opis, rating)
        if CHACKING == True:
            api.AddingANewLine(name_project, status, link, opis, rating)
        else:
            print('WALIDACJA')
            return render_template('add.html', form=form, mess="Popraw błędy w formularzu")
    return render_template('add.html', form=form)

@app.route('/opinions', methods=['Get', 'POST'])
def opinions():
    form = OpinionsForms()
    if request.method == "POST":
        title = request.form.getlist('title')[0]
        comment = request.form.getlist('comment')[0]
        Rating = float(request.form.getlist('rating')[0])
        api.AssessmentOfChanges(title=title, rating=Rating)
        api.AddComment(comment=comment, title=title)
    return render_template('opinions.html', form=form)
if __name__ == '__main__':
    app.run(debug=True)