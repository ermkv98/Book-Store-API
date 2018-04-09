from flask import Flask
from api.v1.Book.controllers import book
from consts import *

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SECRET_KEY'] = SECRET_KEY

app.register_blueprint(book, url_prefix='/Book')

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
