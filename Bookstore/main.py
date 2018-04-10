from flask import Flask
from consts import *
from api.v1.models import db

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SECRET_KEY'] = SECRET_KEY

db.init_app(app)
with app.app_context():
    db.create_all()

from api.v1.Book.controllers import book
from api.v1.User.controllers import user
from api.v1.Transaction.controllers import transaction

app.register_blueprint(book, url_prefix='/Book')
app.register_blueprint(user, url_prefix='/User')
app.register_blueprint(transaction, url_prefix='/Transaction')

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
