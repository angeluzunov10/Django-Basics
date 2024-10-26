from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models

from profiles.validators import UsernameValidator


class Profile(models.Model):
    username = models.CharField(
        max_length=15,
        validators=[
            MinLengthValidator(3, "Username must be at least 3 chars long!"),
            UsernameValidator(),
        ]
    )

    email = models.EmailField()

    age = models.IntegerField(
        MinValueValidator(21)
    )

    password = models.CharField(
        max_length=20
    )

    first_name = models.CharField(
        max_length=25,
        blank=True,
    )

    last_name = models.CharField(
        max_length=25,
        blank=True,
    )

    profile_picture = models.URLField(
        blank=True
    )
