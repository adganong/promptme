from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Genre, PromptPiece, BuiltPrompt, PieceType
from .serializer import GenreSerializer
# Create your views here.


