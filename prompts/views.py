from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, status, mixins
from django.db.models import Q
from .models import Genre, PromptPiece, BuiltPrompt, PieceType
from .serializer import GenreSerializer, PieceTypeSerializer, PromptPieceSerializer, BuiltPromptSerializer
from .toolbelt import models_toolbelt
# NOTE: This will eventually need to be switched to a mix in apparently
# if it is done that way we will get and pot with the same URL... I dunno if I like that
class GenreList(APIView):

    def get(self, request):
        genre = Genre.objects.all()
        serializer = GenreSerializer(genre, many=True)
        return Response(serializer.data)

    # There is no post for this, that is a strategic choice.
    # Any additions to the Genre table MUST be done through the admin view.

    def get_serializer_context(self, *args, **kwargs):
        return {"request": self.request}


class PieceTypeList(APIView):

    def get(self, request):
        piece_type = PieceType.objects.all()
        serializer = PieceTypeSerializer(piece_type, many=True)
        return Response(serializer.data)

    # There is no post for this, that is a strategic choice.
    # Any additions to the Genre table MUST be done through the admin view.

    def get_serializer_context(self, *args, **kwargs):
        return {"request": self.request}


class PromptPieceList(APIView):
    def get(self, request):
        prompt_piece = PromptPiece.objects.all()
        serializer = PromptPieceSerializer(prompt_piece, many=True)
        return Response(serializer.data)

    # There is no post for this, that is a strategic choice.
    # Any additions to the Genre table MUST be done through the admin view.

    def get_serializer_context(self, *args, **kwargs):
        return {"request": self.request}


class BuiltPromptList(APIView):
    def get(self, request):
        built_prompt = BuiltPrompt.objects.all()
        serializer = BuiltPromptSerializer(built_prompt, many=True)
        return Response(serializer.data)

    # There is no post for this, that is a strategic choice.
    # Any additions to the Genre table MUST be done through the admin view.

    def get_serializer_context(self, *args, **kwargs):
        return {"request": self.request}


class GetPromptByType(generics.ListAPIView):
    lookup_field = 'genre'
    serializer_class = PromptPieceSerializer

    def get_queryset(self):
        # This gets the stuff out of the request for me!
        genre_id = self.request.GET.get('genre')
        type_id = self.request.GET.get('type')
        return models_toolbelt.get_piece_based_on_genre_and_type(genre_id, type_id)

