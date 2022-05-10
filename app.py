from flask import Flask
import main

app = Flask(__name__)

@app.route('/')
def index():
    page = ''
    for can in main.load_candidates():
        page += 'Имя кандидата - ' + can['name'] + '\n' + 'Позиция кандидата - ' + can['position'] + '\n'\
                + 'Навыки - ' + can['skills'] + '\n' + '\n'
    return '<pre>' + page + '</pre>'

@app.route('/candidates/<int:uid>')
def candidate(uid):
    candidetes = main.load_candidates()
    if uid > len(candidetes):
        return 'Кандидата с таким номером нет'
    else:
        for can in candidetes:
            if can['id'] == uid:
                return f"""
                <img src = {can['picture']}> <br />
                <p> Имя кандидата - {can['name']} <br />
                <p> Позиция кандидата - {can['position']} <br />
                <p> Навыки - {can['skills']}
                """

@app.route('/skills/<uid>')
def skills_candidate(uid):
    candidetes = main.load_candidates()
    page = ''
    for can in candidetes:
        if uid.lower() in can['skills']:
            page += 'Имя кандидата - ' + can['name'] + '\n' + 'Позиция кандидата - ' + can['position'] + '\n' \
                    + 'Навыки - ' + can['skills'] + '\n' + '\n'
    return '<pre>' + page + '</pre>'


app.run(debug=True)