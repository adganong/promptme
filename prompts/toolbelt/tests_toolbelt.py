from django.test import TestCase
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from rest_framework.reverse import reverse as api_reverse
from django.contrib.auth import get_user_model
from prompts.models import Genre, PromptPiece, BuiltPrompt, PieceType
from . import dict_toolbelt


prompt_info_dict = dict_toolbelt.create_test_dict_instance()


def create_piece_types():
    # This is to set up everything we will be using over the course of the tests
    piece_types = [
        prompt_info_dict['piece_type']['name'][0],
        prompt_info_dict['piece_type']['name'][1],
        prompt_info_dict['piece_type']['name'][2],
        prompt_info_dict['piece_type']['name'][3],
    ]
    to_return = []
    for type_name in piece_types:
        piece_type = PieceType.objects.create(
            piece_type_name=type_name,
        )
        piece_type.save()
        to_return.append(type_name)

    return to_return


def create_genres():
    # This is to set up everything we will be using over the course of the tests
    genres_names = [
        prompt_info_dict['genre']['name'][0],
        prompt_info_dict['genre']['name'][1],
        prompt_info_dict['genre']['name'][2],
        prompt_info_dict['genre']['name'][3],
    ]
    to_return = []
    for genre_name in genres_names:
        genre = Genre.objects.create(
            genre_name=genre_name,
        )
        genre.save()
        to_return.append(genre_name)
    return to_return


def create_prompt_pieces(piece_types, piece_genres):
    # This is to set up everything we will be using over the course of the tests
    piece_name = [
        prompt_info_dict['prompt_piece']['name'][0],
        prompt_info_dict['prompt_piece']['name'][1],
        prompt_info_dict['prompt_piece']['name'][2],
        prompt_info_dict['prompt_piece']['name'][3],
    ]
    piece_description = [
        prompt_info_dict['prompt_piece']['description'][0],
        prompt_info_dict['prompt_piece']['description'][1],
        prompt_info_dict['prompt_piece']['description'][2],
        prompt_info_dict['prompt_piece']['description'][3],
    ]
    piece_type = PieceType.objects.get(piece_type_name=piece_types[0])
    piece_genre = Genre.objects.get(genre_name=piece_genres[0])
    to_return = []

    for i in range(0, 4):
        # This is what I am working on!!!
        # print()
        piece_type = PieceType.objects.get(piece_type_name=piece_types[i])
        prompt_piece = PromptPiece.objects.create(
            piece_type          = piece_type,
            piece_genre         = piece_genre,
            piece_name          = piece_name[i],
            piece_description   = piece_description[i],
        )
        prompt_piece.save()
        to_return.append(prompt_piece)

    return to_return


def create_full_prompt():
    # This will need to query the db based on the 4 types of pieces there are and select one based on each
    # This will be a true to life example of how the actual test will work
    piece_genre  = Genre.objects.get(genre_name="general")
    given_prompt_name = "This is a test prompt"
    # This will need to be changed once more code is developed
    returned_person    = PromptPiece.objects.get(piece_type=PieceType.objects.get(piece_type_name="person"))
    returned_place     = PromptPiece.objects.get(piece_type=PieceType.objects.get(piece_type_name="place"))
    returned_thing     = PromptPiece.objects.get(piece_type=PieceType.objects.get(piece_type_name="thing"))
    returned_scenario  = PromptPiece.objects.get(piece_type=PieceType.objects.get(piece_type_name="scenario"))

    built_prompt        = BuiltPrompt.objects.create(
        prompt_name     = given_prompt_name,
        prompt_person   = returned_person,
        prompt_place    = returned_place,
        prompt_thing    = returned_thing,
        prompt_scenario = returned_scenario,
    )
    built_prompt.save()


def make_and_return_user(username, userpass):
    user_model = get_user_model()
    user = user_model(
        username=username,
        email=username + '@' + username + '.ca'
    )
    user.set_password(userpass)
    user.save()
    return user


def do_full_setup():
    genre_pieces = create_genres()
    piece_types = create_piece_types()
    create_prompt_pieces(piece_types, genre_pieces)
    create_full_prompt()