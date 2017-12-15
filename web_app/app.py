from flask import Flask, render_template
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

from models import db, Page, Menu
from views import PageModelView


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('settings.py')

    db.init_app(app)

    admin = Admin(app, name='Flask01', template_mode='bootstrap3')
    admin.add_view(PageModelView(Page, db.session))
    admin.add_view(ModelView(Menu, db.session))

    @app.route('/')
    @app.route('/<url>')
    def index(url=None):
        print('here', url)
        if url is not None:
            # contoh /about
            page = Page.query.filter_by(url=url).first()
        else:
            # contoh /
            page = Page.query.filter_by(is_homepage=True).first()

        if page is None:
            # TODO cute 404
            return 'Page not found for {} or homepage not set'.format(url)

        contents = 'empty'
        if page is not None:
            contents = page.contents

        menu = Menu.query.order_by('order')


        return render_template('index.html', TITLE='Flask-01', CONTENT=contents, menu=menu)

    return app