from flask_sqlalchemy import SQLAlchemy
from User.consts import PHONE_LENGTH

db = SQLAlchemy()

tr_books = db.Table('tr_books',
                    db.Column('book_id', db.Integer, db.ForeignKey('book.id')),
                    db.Column('tr_id', db.Integer, db.ForeignKey('transaction.id')))


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ISBN_code = db.Column(db.String(13), unique=True)
    name = db.Column(db.String(256))
    price = db.Column(db.Float(precision=2, decimal_return_scale=True))
    category = db.Column(db.String(32))

    def __init__(self, data):
        self.ISBN_code = data['ISBN_code']
        self.name = data['name']
        self.price = data['price']
        self.category = data['category']


class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cost = db.Column(db.Float(precision=2, decimal_return_scale=True))
    books = db.relationship('Book', secondary=tr_books, backref=db.backref('books_tr', lazy='dynamic'))
    user_mail = db.Column(db.String, db.ForeignKey('user.mail'))


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))
    mail = db.Column(db.String(256), unique=True)
    phone_number = db.Column(db.String(PHONE_LENGTH))
    user_tr = db.relationship('Transaction', backref='owner', lazy='dynamic')

    def __init__(self, data):
        self.name = data['name']
        self.mail = data['mail']
        self.phone_number = data['phone_number']
