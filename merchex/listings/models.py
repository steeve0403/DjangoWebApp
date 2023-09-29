from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

class Band(models.Model):

    def __str__(self):
        return f'{self.name}'

    class Genre(models.TextChoices):
        HIP_HOP = 'HH'
        SYNTH_POP = 'SP'
        ALTERNATIVE_ROCK = 'AR'

    name = models.fields.CharField(max_length=100)
    genre = models.fields.CharField(choices=Genre.choices, max_length=5)
    biography = models.fields.CharField(max_length=1000)
    year_formed = models.fields.IntegerField(
       validators=[MinValueValidator(1900),
                   MaxValueValidator(2021)]
    )
    active = models.fields.BooleanField(default=True)
    official_homepage = models.fields.URLField(null=True, blank=True)
    # like_news = models.fields.BooleanField(default=False)

class Listing(models.Model):

    class ListingType(models.TextChoices):
        RECORD = 'R'
        CLOTHING = 'C'
        POSTER = 'P'
        MISC = 'M'

    title = models.fields.CharField(max_length=100)
    description = models.fields.CharField(max_length=100)
    sold = models.fields.BooleanField(default=False)
    year = models.fields.IntegerField(
        validators=[MinValueValidator(1900),
                    MaxValueValidator(2021)]
    )

    type = models.fields.CharField(choices=ListingType.choices, max_length=5)
    band = models.ForeignKey(Band, null=True, on_delete=models.SET_NULL)
