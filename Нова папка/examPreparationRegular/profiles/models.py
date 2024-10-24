from django.core.validators import MinLengthValidator
from django.db import models

from profiles.validators import UsernameValidator


class Profile(models.Model):
    username = models.CharField(
        validators=[
            MinLengthValidator(2),
            UsernameValidator(),
        ],
        max_length=15,
    )

    email = models.EmailField()

    age = models.PositiveIntegerField(
        null=True,
        blank=True
    )
