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


class BasicModelTests(APITestCase):
    # Create your tests here.
    def setUp(self):
        # This is to set up everything we will be using over the course of the tests
        global genre_pieces
        global piece_types
        global prompt_pieces
        genre_pieces = tests_toolbelt.create_genres()
        piece_types = tests_toolbelt.create_piece_types()
        prompt_pieces = tests_toolbelt.create_prompt_pieces(piece_types, genre_pieces)
        tests_toolbelt.create_full_prompt()

    def test_genre_creation(self):
        genre_count = Genre.objects.count()
        self.assertEqual(genre_count, 4)

    def test_piece_type_creation(self):
        type_count = PieceType.objects.count()
        self.assertEqual(type_count, 4)

    def test_prompt_piece_creation(self):
        piece_count = PromptPiece.objects.count()
        self.assertEqual(piece_count, 4)

    def test_full_prompt(self):
        to_show = BuiltPrompt.objects.first()
        print(to_show)
        prompt_count = BuiltPrompt.objects.count()
        self.assertEqual(prompt_count, 1)




