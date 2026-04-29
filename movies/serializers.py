from rest_framework import serializers
from .models import Movie, Genre


# NUEVO
class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = [
            "id",
            "name"
        ]


class MovieSerializer(serializers.ModelSerializer):

    # CAMBIO
    genres = GenreSerializer(
        many=True,
        read_only=True
    )

    class Meta:
        model = Movie
        fields = [
            "id",
            "title",
            "description",
            "release_date",
            "genres"
        ]