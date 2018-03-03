from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Genre, PromptPiece, BuiltPrompt, PieceType
from .serializer import GenreSerializer


class GenreList(APIView):

    def get(self, request):
        genre = Genre.objects.all()
        serializer = GenreSerializer(genre, many=True)
        return Response(serializer.data)

        # There is no post for this, that is a strategic choice.
    # Any additions to the Genre table MUST be done through the admin view.

    def get_serializer_context(self, *args, **kwargs):
        return {"request": self.request}

