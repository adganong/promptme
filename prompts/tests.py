from django.test import TestCase
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from rest_framework.reverse import reverse as api_reverse
from .models import Genre, PromptPiece, BuiltPrompt, PieceType
from prompts.toolbelt import tests_toolbelt
# Pieces to be used throughout the tests
genre_pieces = []
piece_types = []
prompt_pieces = []


class GenreCreationTestCase(APITestCase):
    # Create your tests here.
    def setUp(self):
        # This is to set up everything we will be using over the course of the tests
        global genre_pieces
        genre_pieces = tests_toolbelt.create_genres()
        print(genre_pieces)

    def test_genre_creation(self):
        genre_count = Genre.objects.count()
        self.assertEqual(genre_count, 4)


class PieceTypeCreationTestCase(APITestCase):
    # Create your tests here.
    def setUp(self):
        global piece_types
        piece_types = tests_toolbelt.create_piece_types()
        print(piece_types)

    def test_piece_type_creation(self):
        type_count = PieceType.objects.count()
        self.assertEqual(type_count, 4)


class PromptPieceCreationTestCase(APITestCase):
    # Create your tests here.
    def setUp(self):
        global prompt_pieces
        prompt_pieces = tests_toolbelt.create_prompt_pieces(piece_types, genre_pieces)

    def test_prompt_piece_creation(self):
        piece_count = PromptPiece.objects.count()
        self.assertEqual(piece_count, 4)

