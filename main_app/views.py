from django.shortcuts import render
from .models import Movie

# import HttpResonse to send text-based responses
from django.http import HttpResponse

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def movie_index(request):
  # this line brings in movies from the database
  movies = Movie.objects.all()
  return render(request, 'movies/index.html', {'movies': movies})

def movie_detail(request, movie_id):
  movie = Movie.objects.get(id=movie_id)
  return render(request, 'movies/detail.html', {'movie': movie})