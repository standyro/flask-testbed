from flask import Blueprint, render_template, abort, session, url_for, request, redirect
from jinja2 import TemplateNotFound
from account_model import *



accounts = Blueprint('accounts', __name__,
                     template_folder='templates')


def create_user(username, password):

    new_user = User(username, password)
    db.session.add(new_user)
    db.session.commit()



@accounts.route('/login', methods=['POST','GET'])
def login():
    if request.method == 'POST':
        user = request.form['username']
        password = request.form['password']

        check_user = User.query.filter_by(username=user).first()
        if(check_user):

            if (check_user.authenticate(user, password)):

                session['username'] = user
                return redirect(url_for('index'))

    return render_template("login.html")
                

@accounts.route('/logout', methods=['GET'])
def logout():
    session.pop('username', None)
    return redirect(url_for('accounts.login'))
