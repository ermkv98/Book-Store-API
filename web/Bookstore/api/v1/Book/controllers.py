from flask import Blueprint, jsonify, request
from .models import Book
from .validators import BookSchema

book = Blueprint('Book', __name__)


@book.route('/GetBook', methods=['GET'])
def get_book():
    pass


@book.route('/AddBook', methods=['POST'])
def add_book():
    book_data = request.get_json()
    schema = BookSchema()
    result = schema.load(book_data)
    if result.errors:
        return jsonify(result.errors)
    return 'success'


@book.route('/UpdateBook', methods=['PUT'])
def update_book():
    pass


@book.route('/DeleteBook', methods=['Delete'])
def delete_book():
    pass
