from django.test import TestCase
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from rest_framework.reverse import reverse as api_reverse
from .models import Genre, PromptPiece, BuiltPrompt, PieceType
# Pieces to be used throughout the tests
genre_piece = None
general_genre_piece = None


class GenreAPITestCase(APITestCase):
    # Create your tests here.
    def setUp(self):
        # This is to set up everything we will be using over the course of the tests
        general_genre_piece = Genre.objects.create(
                genre_name='General',
            )
        general_genre_piece.save()

    def test_general_genre(self):
        genre_count = Genre.objects.count()
        self.assertEqual(genre_count, 1)
