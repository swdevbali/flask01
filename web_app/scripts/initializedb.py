import sys, os

sys.path.append(os.getcwd() + '/web_app') #sesuai dengan mark directory as sources

from app import create_app
from models import Page, db

app = create_app()

with app.app_context():
    page = Page()
    page.title = 'Halaman Awal'
    page.contents = "<h1>Selamat datang!</h1>"
    page.is_homepage = True

    db.session.add(page)
    db.session.commit()