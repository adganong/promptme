from django.test import TestCase
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from rest_framework.reverse import reverse as api_reverse
from .models import Genre, PromptPiece, BuiltPrompt, PieceType
from prompts.toolbelt import tests_toolbelt
from django.contrib.auth import get_user_model
# Pieces to be used throughout the tests


class UserCreationTest(APITestCase):
    def setUp(self):
        tests_toolbelt.make_and_return_user('test', 'test')

    def test_genre_creation(self):
        user = get_user_model()
        user_count = user.objects.count()
        self.assertEqual(user_count, 1)


class BasicModelTests(APITestCase):
    def setUp(self):
        tests_toolbelt.do_full_setup()

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
        prompt_count = BuiltPrompt.objects.count()
        self.assertEqual(prompt_count, 1)


class EndPointTests(APITestCase):
    def setUp(self):
        tests_toolbelt.do_full_setup()
        user = tests_toolbelt.make_and_return_user('testuser', 'testpass')

    def test_get_genres(self):
        pass



