from flask import Flask


def create_app():
    app = Flask(__name__)

    @app.route('/')
    def index():
        return 'Halo flask, ini hot reload ya!'

    @app.route('/about')
    def about():
        return 'About me'

    return app