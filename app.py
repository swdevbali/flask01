from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'Halo flask'


@app.route('/about')
def about():
    return 'About me'

app.run('0.0.0.0', debug=True)