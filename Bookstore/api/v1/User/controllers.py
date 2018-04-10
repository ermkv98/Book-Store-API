from flask import Blueprint, jsonify, request
from ..models import User, db
from .validators import FullUserSchema, ShortUserSchema

user = Blueprint('User', __name__)


@user.route('/AddUser', methods=['POST'])
def add_user():
    user_data = request.get_json()
    user = User.query.filter_by(mail=user_data['mail']).first()
    if user:
        return jsonify({'error': 'user with mail {} already exists'.format(user.mail)}), 400
    schema = FullUserSchema()
    result = schema.load(user_data)
    if result.errors:
        return jsonify(result.errors)
    user = User(user_data)
    db.session.add(user)
    db.session.commit()
    response = jsonify({'created': schema.dump(user)}), 201
    return response


@user.route('/GetUser', methods=['GET'])
def get_user():
    user_data = request.get_json()
    schema = ShortUserSchema()
    result = schema.load(user_data)
    if result.errors:
        return jsonify(result.errors)
    user = User.query.filter_by(mail=user_data['mail']).first()
    if user:
        schema = FullUserSchema()
        response = jsonify({'user found': schema.dump(user)}), 200
    else:
        response = jsonify({'error': 'not found'}), 404
    return response


@user.route('/DeleteUser', methods=['DELETE'])
def delete_user():
    user_data = request.get_json()
    schema = ShortUserSchema()
    result = schema.load(user_data)
    if result.errors:
        return jsonify(result.errors)
    user = User.query.filter_by(mail=user_data['mail']).first()
    if user:
        response = jsonify({'deleted': 'successfully deleted'}), 200
        db.session.delete(user)
        db.session.commit()
    else:
        response = jsonify({'error': 'not found'}), 404
    return response
