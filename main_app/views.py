from django.shortcuts import render

# import HttpResonse to send text-based responses
from django.http import HttpResponse

class Movie:
  def __init__(self, title, director, year, genre, rating):
    self.title = title
    self.director = director
    self.year = year
    self.genre = genre
    self.rating = rating

movies = [
  Movie('Kpop Demon Hunters', 'Maggie Kang', 2025, 'Animation', 10.0),
  Movie("Parasite", "Bong Joon-ho", 2019, "Thriller", 8.6),
  Movie("Train to Busan", "Yeon Sang-ho", 2016, "Action", 7.6),
]

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def movie_index(request):
  movies = Movie.object.all()
  return render(request, 'movies/index.html', {'movies': movies})
