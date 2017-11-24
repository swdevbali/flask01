from flask import Flask, render_template

from web_app.models import db, Page


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('settings.py')

    db.init_app(app)

    @app.route('/')
    def index():
        page = Page.query.filter_by(id=1).first()

        return render_template('index.html', TITLE='Flask-01', CONTENT=page.contents)

    @app.route('/about')
    def about():
        return render_template('about.html', TITLE='Flask-01')

    @app.route('/testdb')
    def testdb():
        import psycopg2

        con = psycopg2.connect('dbname=flask01 user=devuser password=devpassword host=postgres')
        cur = con.cursor()

        cur.execute('select * from page;')

        id, title = cur.fetchone()
        con.close()
        return 'Output table page: {} - {}'.format(id, title)

    return app