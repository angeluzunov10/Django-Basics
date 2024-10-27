import re

from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


@deconstructible
class NameValidator:
    def __init__(self, message=None):
        self.message = message

    @property
    def message(self):
        return self.__message

    @message.setter
    def message(self, value):
        if value is None:
            self.__message = "Your name must contain letters only!"
        else:
            self.__message = value

    def __call__(self, value, *args, **kwargs):
        if not re.match(r"^[A-Za-z]*$", value):
            raise ValidationError(self.message)


@deconstructible
class PasswordLengthValidator:
    def __init__(self, message=None):
        self.message = message

    @property
    def message(self):
        return self.__message

    @message.setter
    def message(self, value):
        if value is None:
            self.__message = "Your passcode must be exactly 6 digits!"
        else:
            self.__message = value

    def __call__(self, value, *args, **kwargs):
        if not re.match(r"^\d{6}$", value):
            raise ValidationError(self.message)