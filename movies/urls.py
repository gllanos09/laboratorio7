from django.urls import path
from .views import (
    MovieListView,
    GenreListView
)


urlpatterns = [
    path(
        "movies/",
        MovieListView.as_view(),
        name="movie-list"
    ),

    # NUEVO
    path(
        "genres/",
        GenreListView.as_view(),
        name="genre-list"
    ),
]