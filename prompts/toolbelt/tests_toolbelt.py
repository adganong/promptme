from django.test import TestCase
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from rest_framework.reverse import reverse as api_reverse
from prompts.models import Genre, PromptPiece, BuiltPrompt, PieceType

# Pieces to be used throughout the tests
# These are functions to be used in the tests


def create_piece_types():
    # This is to set up everything we will be using over the course of the tests
    piece_types = ['person', 'place', 'thing', 'scenario']
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
    genres_names = ['general', 'sci-fi', 'fantasy', 'thriller']
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
    piece_name = ['Retired Captain', 'A Market', 'A Computer', 'Something has been lost']
    piece_description = ['description 1', 'description 2', 'description 3', 'description 4']
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

    returned_person     = PromptPiece.get_random_by_genre(piece_genre_id=piece_genre.id)
    returned_place      = PromptPiece.get_random_by_genre(piece_genre_id=piece_genre.id)
    returned_thing      = PromptPiece.get_random_by_genre(piece_genre_id=piece_genre.id)
    returned_scenario   = PromptPiece.get_random_by_genre(piece_genre_id=piece_genre.id)

    built_prompt        = BuiltPrompt.objects.create(
        prompt_person   = returned_person,
        prompt_place    = returned_place,
        prompt_thing    = returned_thing,
        prompt_scenario = returned_scenario,
    )
    built_prompt.save()

