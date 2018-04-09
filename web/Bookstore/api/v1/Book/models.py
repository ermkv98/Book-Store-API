from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ISBN_code = db.Column(db.Integer, unique=True)
    name = db.Column(db.String(256))
    price = db.Column(db.Float(precision=2, decimal_return_scale=True))
    categories = db.Column(db.String)

    def __init__(self, ISBN_code, name, price):
        self.ISBN_code = ISBN_code
        self.name = name
        self.price = price
        self.tags = []

    def add_tags(self, **kw):
        for k in kw:
            self.tags.append(k)


