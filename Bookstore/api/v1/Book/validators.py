from marshmallow import fields, Schema, ValidationError, validates
from .consts import *
import re


class FullBookSchema(Schema):
    ISBN_code = fields.String(required=True)
    name = fields.String(required=True)
    price = fields.Float(required=True, precision=2, decimal_return_scale=True)
    category = fields.String()

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

    @validates('category')
    def validate_category(self, category):
        if category not in CATEGORIES:
            raise ValidationError('Categories restricted: {}'.format(CATEGORIES))


class ShortBookSchema(Schema):
    ISBN_code = fields.String(required=True)

    @validates('ISBN_code')
    def validate_code(self, ISBN_code):
        if len(ISBN_code) is not ISBN_CODE_LENGTH:
            raise ValidationError('ISBN_code must contain {} characters'.format(ISBN_CODE_LENGTH))
        if re.match(r'[^\d-]', ISBN_code):
            raise ValidationError('ISBN_code must contain only numbers and dashes')


class FilterSchema(Schema):
    category = fields.String()
    price_min = fields.Float(precision=2, decimal_return_scale=True)
    price_max = fields.Float(precision=2, decimal_return_scale=True)

    def validate_price_min(self, price_min):
        if price_min < MIN_BOOK_PRICE:
            raise ValidationError('Price should be higher than {}'.format(MIN_BOOK_PRICE))

    def validate_price_max(self, price_max):
        if price_max < MIN_BOOK_PRICE:
            raise ValidationError('Price should be higher than {}'.format(MIN_BOOK_PRICE))
