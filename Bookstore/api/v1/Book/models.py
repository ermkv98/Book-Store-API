from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ISBN_code = db.Column(db.Integer, unique=True)
    name = db.Column(db.String(256))
    price = db.Column(db.Float(precision=2, decimal_return_scale=True))
    categories = db.Column(db.String(256))

    def __init__(self, data):
        self.ISBN_code = data['ISBN_code']
        self.name = data['name']
        self.price = data['price']

    def add_categories(self, category):
        if self.categories is None:
            self.categories = category
        else:
            self.categories += ', ' + category
