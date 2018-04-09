from flask import Blueprint, jsonify, request
from .models import Book, db
from .validators import FullBookSchema, ShortBookSchema

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
    book.add_categories(book_data['categories'])
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
