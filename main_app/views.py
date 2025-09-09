from django.shortcuts import render

# import HttpResonse to send text-based responses
from django.http import HttpResponse

def home(request):
  return HttpResponse('<h1>Hello, this is my movie app!</h1>')

def about(request):
  return HttpResponse('<h1>This is the about page</h1>')
  # return render(request, 'about.html')

# def movies_index(request):
#   movies = Movie.object.all()
#   return render(request, 'movies/index.html', {'movies': movies})
