from django.contrib import admin

# Register your models here.
from .models import Actor
from .models import Movie
admin.site.register(Actor)
admin.site.register(Movie)