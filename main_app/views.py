from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Movie
from .forms import ActorForm
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# import HttpResonse to send text-based responses
from django.http import HttpResponse

class Home(LoginView):
  template_name = 'home.html'

def about(request):
  return render(request, 'about.html')

@login_required
def movie_index(request):
  movies = Movie.objects.filter(user=request.user)
  return render(request, 'movies/index.html', {'movies': movies})

@login_required
def movie_detail(request, movie_id):
  movie = Movie.objects.get(id=movie_id)
  actor_form = ActorForm()
  return render(request, 'movies/detail.html', {'movie': movie, 'actor_form': actor_form})

class MovieCreate(LoginRequiredMixin, CreateView):
  model = Movie
  fields = '__all__'
def form_valid(self, form):
  # Assign the logged in user (self.request.user)
  form.instance.user = self.request.user  
  # form.instance is the movie
  # Let the CreateView do its job as usual
  return super().form_valid(form)

class MovieUpdate(LoginRequiredMixin, UpdateView):
  model = Movie
  fields = '__all__'

class MovieDelete(LoginRequiredMixin, DeleteView):
  model = Movie
  success_url = '/movies/'

@login_required
def add_actor(request, movie_id):
    form = ActorForm(request.POST)
    if form.is_valid():
        new_actor = form.save(commit=False)
        new_actor.movie_id = movie_id
        new_actor.save()
    return redirect('movie-detail', movie_id=movie_id)

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('movie-index')
  else:
    error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'signup.html', context)
