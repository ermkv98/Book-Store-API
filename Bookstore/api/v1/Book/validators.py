from marshmallow import fields, Schema, ValidationError, validates
from .consts import *
import re


class BookSchema(Schema):
    ISBN_code = fields.String(required=True)
    name = fields.String(required=True)
    price = fields.Float(required=True)
    categories = fields.String()

    @validates('ISBN_code')
    def validate_code(self, ISBN_code):
        if len(ISBN_code) is not ISBN_CODE_LENGTH:
            raise ValidationError('ISBN_code must contain {} characters'.format(ISBN_CODE_LENGTH))
        if re.match(r'[^\d-]', ISBN_code):
            raise ValidationError('ISBN_code must contain only numbers and dashes')

    @validates('price')
    def validate_price(self, price):
        if not price:
            raise ValidationError('Price not defined')
        if price < MIN_BOOK_PRICE:
            raise ValidationError('Price should be higher than {}'.format(MIN_BOOK_PRICE))

    @validates('categories')
    def validate_categories(self, categories):
        if not categories:
            raise ValidationError('Category not defined')
        if len(categories) > CATEGORY_LENGTH:
            raise ValidationError('Category must be no longer than {} characters'.format(CATEGORY_LENGTH))
        if re.match(r'[^a-zA-z ]', categories):
            raise ValidationError('Category must contain only string characters')
