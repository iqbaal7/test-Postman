from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.


class Band(models.Model):
    name = models.fields.CharField(max_length=100)
    genre = models.fields.CharField(max_length=100)
    biography = models.fields.CharField(max_length=1000)
    year_formed = models.fields.IntegerField(
    validators=[MinValueValidator(1900), MaxValueValidator(2024)]
    )
    active = models.fields.BooleanField(default=True)
    official_homepage = models.fields.URLField(null=True, blank=True)
    def __str__(self):
        return f'{self.name}'
    
class Genre(models.TextChoices):
    HIP_HOP = 'HH'
    SYNTH_POP = 'SP'
    ALTERNATIVE_ROCK = 'AR' 
genre = models.fields.CharField(choices=Genre.choices, max_length=5)

class Listing(models.Model):
    band = models.ForeignKey(Band, null=True, on_delete=models.SET_NULL)


    
    
    