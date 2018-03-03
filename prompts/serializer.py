from rest_framework import serializers
from .models import PromptPiece, BuiltPrompt, Genre, PieceType


class GenreSerializer(serializers.ModelSerializer):
    # url = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Genre
        # Do not use this, but everything can be returned by using
        # fields = '__all__'
        fields = (
            'pk',
            'genre_name',
            'parent_id',
        )

        # If URL is added, it should also be added here
        read_only_fields = ['pk']

    # Url stuff? I don't exactly get what this is meant to do though
    # Okay, I get this now. It is grabbing the url and putting it into the 'url' field
    # it knows where to put it because the format is get_<arg> and that function will auto fill in my fields
    # This is not really needed for what I am doing here actually

    # def get_url(self, obj):
    #    request = self.context.get("request")
    #    return obj.get_api_url()


class PieceTypeSerializer(serializers.ModelSerializer):

    class Meta:
        # I am not surre what this is, nor why exactly it is here. I think it has to do with putting info
        model = PieceType

        fields = (
            'pk',
            'piece_type_name',
        )
        read_only_fields = ['pk', 'piece_type_name']


class PromptPieceSerializer(serializers.ModelSerializer):
    class Meta:
        model = PromptPiece

        fields = (
            'pk',
            'piece_type',
            'piece_genre',
            'piece_name',
            'piece_description',
        )
        read_only_fields = ['pk']


class BuiltPromptSerializer(serializers.ModelSerializer):
    pass
