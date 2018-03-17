from django.test import TestCase
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from rest_framework.reverse import reverse as api_reverse
from .models import Genre, PromptPiece, BuiltPrompt, PieceType
from prompts.toolbelt import tests_toolbelt, models_toolbelt, dict_toolbelt
from django.contrib.auth import get_user_model
from .serializer import PromptPieceSerializer
# Pieces to be used throughout the tests

# initialize this variable to be used in every test
prompt_info_dict = dict_toolbelt.create_test_dict_instance()


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


    def test_get_retrieve_single_prompt_piece_by_type(self):
        # todo this test needs to be changed so that it queries to find out what the genre id is
        # todo My dictionary is all fucked up. It is giving everything a genre id of 1
        # todo tests are broken. The setup class needs to be modified before I proceed with them
        response = models_toolbelt.get_piece_based_on_genre_and_type(9, 9)
        self.assertEqual(len(response), 1)


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
        data = {}
        url = api_reverse("api-genres:genres-list")
        response = self.client.get(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 4)


    def test_get_piece_types(self):
        data = {}
        url = api_reverse("api-piece_types:piece_types-list")
        response = self.client.get(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 4)

    def test_get_prompt_pieces(self):
        data = {}
        url = api_reverse("api-prompt_pieces:prompt_pieces-list")
        response = self.client.get(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 4)

    def test_get_built_prompts(self):
        data = {}
        url = api_reverse("api-built_prompts:built_prompts-list")
        response = self.client.get(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

