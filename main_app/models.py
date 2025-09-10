from django.db import models
from django.urls import reverse
from django.core.validators import MinValueValidator, MaxValueValidator

GENRES = (
  ('ACTION', 'Action'),
  ('COMEDY', 'Comedy'),
  ('DRAMA', 'Drama'),
  ('HORROR', 'Horror'),
  ('SCI-FI', 'Sci-Fi'),
)

class Movie(models.Model):
  title = models.CharField(max_length=100)
  director = models.CharField(max_length=100)
  year = models.IntegerField()
  description = models.TextField(max_length=250)
  genre = models.CharField(
    choices = GENRES,
    default = GENRES[0][0]
  )
  rating = models.IntegerField(
    validators=[MinValueValidator(0), MaxValueValidator(10)]
  )