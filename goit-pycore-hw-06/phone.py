from field import Field
import re

class Phone(Field):
    def __init__ (self, value):
        self.validate(value)
        super().__init__(value)

    @staticmethod
    def validate(self, value):
        if not re.fullmatch(r'/d{10}', value):
            raise ValueError('Invalid phone number')