from django.db import models
from django.urls import reverse
from django.core.validators import MinValueValidator, MaxValueValidator

GENRES = (
  ('ACTION', 'Action'),
  ('COMEDY', 'Comedy'),
  ('DRAMA', 'Drama'),
  ('HORROR', 'Horror'),
  ('ANIMATION', 'Animation'),
  ('THRILLER', 'Thriller'),
  ('ROMANCE', 'Romance'),
  ('MYSTERY', 'Mystery'),
  ('CRIME', 'Crime'),
  ('FANTASY', 'Fantasy'),
  ('HISTORICAL', 'Historical'),
  ('WAR', 'War'),
  ('SPORTS', 'Sports'),
  ('SCI-FI', 'Sci-Fi'),
)

class Movie(models.Model):
  title = models.CharField(max_length=100)
  year = models.IntegerField()
  description = models.TextField(max_length=250)
  genre = models.CharField(
    max_length=20,
    choices = GENRES,
    default = GENRES[0][0]
  )
  rating = models.IntegerField(
    validators=[MinValueValidator(0), MaxValueValidator(10)]
  )

  def __str__(self):
    return self.title
  
  def get_absolute_url(self):
    return reverse('movie-detail', kwargs={'movie_id': self.id})
  
class Actor(models.Model):
  name = models.CharField(max_length=50)
  role = models.CharField(max_length=100)

  movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

  def __str__(self):
    return self.name