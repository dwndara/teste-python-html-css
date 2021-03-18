from app import app
from flask import render_template


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Dandara'}
    posts = [
        {'author': {'username': 'Jully'}, 'body': "Rocketzada??"},
        {'author': {'username': 'Luiz'}, 'body': "Vavazada??"},
        {'author': {'username': 'Fábio'}, 'body': "Rocketzada!!!"},
    ]
    return render_template("index.html", user=user, posts=posts)