from flask import Flask
from api.v1.Book.controllers import book, db as book_db
from api.v1.User.controllers import user, db as user_db
from consts import *

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SECRET_KEY'] = SECRET_KEY

app.register_blueprint(book, url_prefix='/Book')
app.register_blueprint(user, url_prefix='/User')

with app.app_context():
    book_db.init_app(app)
    book_db.create_all()
    user_db.create_all()

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
