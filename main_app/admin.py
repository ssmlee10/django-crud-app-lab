from django.contrib import admin
from .models import Movie, Actor

# Register your models here.
# this brings in the movie model into the admin site
admin.site.register(Movie)
admin.site.register(Actor)