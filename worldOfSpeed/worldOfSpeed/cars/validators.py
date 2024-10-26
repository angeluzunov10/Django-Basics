from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


@deconstructible
class YearValidator:
    def __init__(self, min_year=1999, max_year=2030, message=None):
        self.min_year = min_year
        self.max_year = max_year
        self.message = message or f"The year must be between {self.min_year} and {self.max_year}!"

    @property
    def message(self):
        return self._message

    @message.setter
    def message(self, value):
        self._message = value

    def __call__(self, value):
        if not (self.min_year <= value <= self.max_year):
            raise ValidationError(self.message)
