from myapp.main import main
from flask import render_template


@main.route('/')
def index():
    return '<h1>Hello World from app factory!</h1>'


@main.route('/hello')
@main.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)
