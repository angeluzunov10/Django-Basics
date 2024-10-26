from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models

from cars.choices import CarTypeChoices
from cars.validators import YearValidator
from profiles.models import Profile


class Car(models.Model):
    type = models.CharField(
        max_length=10,
        choices=CarTypeChoices.choices
    )

    model = models.CharField(
        max_length=15,
        validators=[
            MinLengthValidator(1)
        ]
    )

    year = models.IntegerField(
        validators=[
            YearValidator(),
        ]
    )

    image_url = models.URLField(
        unique=True,
    )

    price = models.FloatField(
        MinValueValidator(1.0)
    )

    owner = models.ForeignKey(
        to="profiles.Profile",
        on_delete=models.CASCADE,
        editable=False,
        related_name="cars",
    )