from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('settings.py')

    db = SQLAlchemy(app)

    class Page(db.Model):
        __tablename__ = 'page'
        id = Column(Integer, primary_key=True)
        tag = Column(String)
        contents = Column(String)

    class Post(db.Model):
        __tablename__ = 'post'
        id = Column(Integer, primary_key=True)
        contents = Column(String)
    db.create_all()

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