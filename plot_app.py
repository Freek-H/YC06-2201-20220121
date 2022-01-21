from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/html')
def hello_html():
    return render_template('hello.html')


@app.route('/template')
def template():
    return render_template('template.html', tekst='Dit is nu deze tekst')