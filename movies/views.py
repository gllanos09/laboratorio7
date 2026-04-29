from rest_framework import generics
from .models import Movie, Genre
from .serializers import (
    MovieSerializer,
    GenreSerializer
)


class MovieListView(generics.ListAPIView):

    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


# NUEVO
class GenreListView(generics.ListAPIView):

    queryset = Genre.objects.all()
    serializer_class = GenreSerializer