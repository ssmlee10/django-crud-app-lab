from django.shortcuts import render

# import HttpResonse to send text-based responses
from django.http import HttpResponse

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

# def movies_index(request):
#   movies = Movie.object.all()
#   return render(request, 'movies/index.html', {'movies': movies})
