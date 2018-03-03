from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Genre, PromptPiece, BuiltPrompt, PieceType
from .serializer import GenreSerializer, PieceTypeSerializer, PromptPieceSerializer, BuiltPromptSerializer


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
    pass
