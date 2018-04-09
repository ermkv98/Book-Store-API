from marshmallow import fields, Schema, ValidationError, validates
import re
from .consts import *


class FullUserSchema(Schema):
    name = fields.String(required=True)
    mail = fields.Email(required=True)
    phone_number = fields.String(required=True)

    @validates('phone_number')
    def validate_code(self, phone_number):
        if len(phone_number) is not PHONE_LENGTH:
            raise ValidationError('Phone must contain {} characters'.format(PHONE_LENGTH))
        if re.match(r'[^\d]', phone_number):
            raise ValidationError('Phone must contain only numbers')


class ShortUserSchema(Schema):
    mail = fields.Email(required=True)
