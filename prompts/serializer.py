from rest_framework import serializers
from .models import PromptPiece, BuiltPrompt, Genre, PieceType


class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        # Do not use this, but everything can be returned by using
        # fields = '__all__'
        fields = (
            'genre_name',
            'parent_id',
        )
