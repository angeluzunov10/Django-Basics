from django.core.validators import MinLengthValidator
from django.db import models

from authors.validators import NameValidator, PasswordLengthValidator


class Author(models.Model):
    first_name = models.CharField(
        max_length=40,
        validators=[
            MinLengthValidator(4),
            NameValidator(),
        ]
    )

    last_name = models.CharField(
        max_length=50,
        validators=[
            MinLengthValidator(2),
            NameValidator(),
        ]
    )

    passcode = models.CharField(
        validators=[
            PasswordLengthValidator()
        ],
        help_text='Your passcode must be a combination of 6 digits'
    )

    pets_number = models.PositiveSmallIntegerField()

    info = models.TextField(blank=True)

    image_url = models.URLField(blank=True)

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

