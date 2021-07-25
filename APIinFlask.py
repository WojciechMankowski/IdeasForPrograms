from flask import Flask, render_template, request
from test import NotionAPISupport
from Forms import Forms
app = Flask(__name__)
api = NotionAPISupport()

@app.route("/")
def home():
    resultat = api.GetInformation()
    return resultat
@app.route('/add', methods=['Get', 'POST'])
def addItems():
    # print()
    if request.method == "POST":
        form = request.form
        title = form['title']
        status = form['status']
        print(status)
        if form['link'] == '':
            link = None
        else:
            link = form['link']
        if form['opis'] == '':
            opis = None
        else:
            opis = form['opis']
        # print(title,status,link,opis)
        # api.AddingANewLine(title,status,link,opis)
    return render_template('todolist.html')

@app.route('/test', methods=['Get', 'POST'])
def test():
    form = Forms()
    Form = request.form

    name_project = Form.getlist('name_project')[0]
    status = Form.getlist('status')[0]
    link = Form.getlist('link')[0]
    opis = Form.getlist('opis')[0]
    rating= int(Form.getlist('rating')[0])

    # name_project = Form['name_project']
    # status = Form['status ']
    # link = Form['link']
    # opis = Form['opis']
    # rating = Form['rating']
    return render_template('test.html',  form=form)
if __name__ == '__main__':
    app.run(debug=True)