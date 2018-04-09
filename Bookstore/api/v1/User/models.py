from flask_sqlalchemy import SQLAlchemy
from .consts import *

db = SQLAlchemy()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))
    mail = db.Column(db.String(256), unique=True)
    phone_number = db.Column(db.String(PHONE_LENGTH))

    def __init__(self, data):
        self.name = data['name']
        self.mail = data['mail']
        self.phone_number = data['phone_number']
