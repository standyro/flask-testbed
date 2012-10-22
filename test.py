from flask import Flask, url_for, redirect, session, render_template
from accounts import *


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.secret_key = 'giraffesandcatsaredabomb'

app.register_blueprint(accounts)
db.init_app(app)


def init_db():
    db.create_all(app=app)


@app.route("/")
def index():
    if 'username' in session:
        return "What's up"
    return redirect(url_for('accounts.login'))



if __name__ == '__main__':
    app.debug = True
    app.run()
    
