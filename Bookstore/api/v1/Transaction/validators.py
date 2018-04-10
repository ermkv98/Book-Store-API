from marshmallow import fields, Schema, ValidationError, validates
import re
from .consts import *


class FullTransactionSchema(Schema):
    mail = fields.Email(required=True)
    Books_ISBNs = fields.List(fields.String())

    @validates('Books_ISBNs')
    def validate_ISBNs(self, Books_ISBNs):
        for Book in Books_ISBNs:
            if len(Book) is not ISBN_CODE_LENGTH:
                raise ValidationError('ISBN_code must contain {} characters'.format(ISBN_CODE_LENGTH))
            if re.match(r'[^\d-]', Book):
                raise ValidationError('ISBN_code must contain only numbers and dashes')


class ShortTransactionSchema(Schema):
    id = fields.Integer()


class BookSchema(Schema):
    ISBN_code = fields.String()
    name = fields.String()
    price = fields.Float()
    category = fields.String()


class GetTransactionSchema(Schema):
    user_mail = fields.String()
    books = fields.Nested(BookSchema, many=True)
    cost = fields.Float()
