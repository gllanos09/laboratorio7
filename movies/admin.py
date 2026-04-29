from django.contrib import admin
from .models import Movie, Genre


# CAMBIO
admin.site.register(Movie)
admin.site.register(Genre)