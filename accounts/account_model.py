import os
import hashlib
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
'''
Account Model module contains the code for manipulating account data.
This involves adding editing and deleting accounts
'''

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    db.init_app(app)
    return app


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(800), unique=True)
    salt = db.Column(db.String(512))

    def __init__(self, username, password):
        self.username = username
        self.salt = unicode(os.urandom(32), errors='ignore')
        self.password = self.encrypt(password, self.salt)

        
    def __repr__(self):
        return '<User %r>' % self.username

    
    def encrypt(self, password, salt):
        print salt
        return hashlib.sha512(salt+password).hexdigest()
    
    
    def authenticate(self, username, password):
        if (self.username == username):
            if (self.encrypt(password, self.salt) == self.password):
                return True
            
        return False

