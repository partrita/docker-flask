#!flask/bin/python
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def hello():
    return render_template('app.html')


@app.route('/tools')
def tools():
    pass


if __name__ == '__main__':
    app.run(host='0.0.0.0')
