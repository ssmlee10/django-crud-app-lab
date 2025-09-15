from django.urls import path, include
from . import views

urlpatterns = [
  path('', views.Home.as_view(), name='home'),
  path('about/', views.about, name='about'),
  path('movies/', views.movie_index, name='movie-index'),
  path('movies/<int:movie_id>/', views.movie_detail, name='movie-detail'),
  path('movies/create/', views.MovieCreate.as_view(), name='movie-create'),
  path('movies/<int:pk>/update/', views.MovieUpdate.as_view(), name='movie-update'),
  path('movies/<int:pk>/delete', views.MovieDelete.as_view(), name='movie-delete'),
  path('movies/<int:movie_id>/add-actor/', views.add_actor, name='add-actor'),
  path('accounts/', include('django.contrib.auth.urls')),
]