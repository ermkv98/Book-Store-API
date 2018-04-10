from flask import Blueprint, jsonify, request
from ..models import Transaction, Book, User, db
from .validators import FullTransactionSchema, ShortTransactionSchema, GetTransactionSchema

transaction = Blueprint('Transaction', __name__)


@transaction.route('/Create', methods=['POST'])
def create_transaction():
    tr_data = request.get_json()
    schema = FullTransactionSchema()
    result = schema.load(tr_data)
    if result.errors:
        return jsonify(result.errors)
    tr = Transaction()
    tr.cost = 0
    error_list = ""
    user = User.query.filter_by(mail=tr_data['mail']).first()
    if not user:
        return jsonify({'error': 'user with mail {} does not exists'.format(tr_data['mail'])}), 400
    else:
        tr.user_mail = tr_data['mail']
    if 'Books_ISBNs' in tr_data:
        for ISBN_code in tr_data['Books_ISBNs']:
            book = Book.query.filter_by(ISBN_code=ISBN_code).first()
            if book:
                tr.books.append(book)
                tr.cost += book.price
            else:
                error_list += ' {}'.format(ISBN_code)
    db.session.add(tr)
    db.session.commit()
    response = jsonify({'Status': 'Success',
                        'Cost': tr.cost,
                        'ISBNs not found:': error_list,
                        'Transaction id': tr.id}), 201
    return response


@transaction.route('/Get', methods=['GET'])
def get_transaction():
    tr_data = request.get_json()
    schema = ShortTransactionSchema()
    result = schema.load(tr_data)
    if result.errors:
        return jsonify(result.errors)
    tr = Transaction.query.filter_by(id=tr_data['id']).first()
    if tr:
        schema = GetTransactionSchema()
        response = jsonify({'Transaction found': schema.dump(tr)}), 200
    else:
        response = jsonify({'error': 'not found'}), 404
    return response


@transaction.route('/Delete', methods=['DELETE'])
def delete_transaction():
    tr_data = request.get_json()
    schema = ShortTransactionSchema()
    result = schema.load(tr_data)
    if result.errors:
        return jsonify(result.errors)
    tr = Transaction.query.filter_by(id=tr_data['id']).first()
    if tr:
        response = jsonify({'Deleted': 'successfully deleted'}), 200
        db.session.delete(tr)
        db.session.commit()
    else:
        response = jsonify({'error': 'not found'}), 404
    return response
