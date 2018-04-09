from flask import Blueprint, jsonify, request
from .models import Book, db
from .validators import BookSchema

book = Blueprint('Book', __name__)


@book.route('/GetBook', methods=['GET'])
def get_book():
    pass


@book.route('/AddBook', methods=['POST'])
def add_book():
    book_data = request.get_json()
    book = Book.query.filter_by(ISBN_code=book_data['ISBN_code']).first()
    if book:
        return jsonify({'error': 'book with ISBN {} already exists'.format(book.ISBN_code)}), 400
    schema = BookSchema()
    result = schema.load(book_data)
    if result.errors:
        return jsonify(result.errors)
    book = Book(book_data)
    book.add_categories(book_data['categories'])
    db.session.add(book)
    db.session.commit()
    response = jsonify({'created': schema.dump(book)}), 201
    return response


@book.route('/UpdateBook', methods=['PUT'])
def update_book():
    pass


@book.route('/DeleteBook', methods=['Delete'])
def delete_book():
    pass
