from flask import Blueprint, jsonify, request
from ..models import Book, db
from sys import maxint
from .validators import FullBookSchema, ShortBookSchema, FilterSchema
from .consts import MIN_BOOK_PRICE

book = Blueprint('Book', __name__)


@book.route('/GetBook', methods=['GET'])
def get_book():
    book_data = request.get_json()
    schema = ShortBookSchema()
    result = schema.load(book_data)
    if result.errors:
        return jsonify(result.errors)
    book = Book.query.filter_by(ISBN_code=book_data['ISBN_code']).first()
    if book:
        schema = FullBookSchema()
        response = jsonify({'book found': schema.dump(book)}), 200
    else:
        response = jsonify({'error': 'not found'}), 404
    return response


@book.route('/AddBook', methods=['POST'])
def add_book():
    book_data = request.get_json()
    book = Book.query.filter_by(ISBN_code=book_data['ISBN_code']).first()
    if book:
        return jsonify({'error': 'book with ISBN {} already exists'.format(book.ISBN_code)}), 400
    schema = FullBookSchema()
    result = schema.load(book_data)
    if result.errors:
        return jsonify(result.errors)
    book = Book(book_data)
    db.session.add(book)
    db.session.commit()
    response = jsonify({'created': schema.dump(book)}), 201
    return response


@book.route('/DeleteBook', methods=['Delete'])
def delete_book():
    book_data = request.get_json()
    schema = ShortBookSchema()
    result = schema.load(book_data)
    if result.errors:
        return jsonify(result.errors)
    book = Book.query.filter_by(ISBN_code=book_data['ISBN_code']).first()
    if book:

        response = jsonify({'deleted': 'successfully deleted'}), 200
        db.session.delete(book)
        db.session.commit()
    else:
        response = jsonify({'error': 'not found'}), 404
    return response


@book.route('/GetAllBooks', methods=['GET'])
def get_all():
    book_data = request.get_json()
    schema = FilterSchema()
    result = schema.load(book_data)
    if result.errors:
        return jsonify(result.errors)
    books = Book.query.all()
    if book_data:
        if 'price_min' in book_data:
            price_min = book_data['price_min']
        else:
            price_min = MIN_BOOK_PRICE
        if 'price_max' in book_data:
            price_max = book_data['price_max']
        else:
            price_max = maxint
        if 'category' in book_data:
            books = Book.query.filter_by(category=book_data['category']). \
                filter(Book.price >= price_min). \
                filter(Book.price <= price_max)
        else:
            books = Book.query.filter(Book.price >= price_min). \
                filter(Book.price <= price_max)
    schema = FullBookSchema(many=True)
    if books:
        result = schema.dump(books)
        response = jsonify({'books': result}), 200
    else:
        response = jsonify({'error': 'not found'}), 404
    return response
