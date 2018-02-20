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
        to_return.append(piece_type)

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
        to_return.append(genre)

    return to_return

def gm(obj, param):
    object = Genre.objects.filter(pub_date__year=param)
    return object

def create_prompt_pieces(piece_types, piece_genres):
    # This is to set up everything we will be using over the course of the tests
    piece_name = ['Retired Captain', 'A Market', 'A Computer', 'Something has been lost']
    piece_description = ['description 1', 'description 2', 'description 3', 'description 4']
    to_return = []

    for i in range(0, 4):
        print("this" + str(i))
        # This is what I am working on!!!
        this_thing = PieceType.objects.filter(piece_type_name=piece_types[i])
        print(this_thing.piece_type_name)
        # print()
        '''prompt_piece = PromptPiece.objects.create(
    piece_type          = PieceType.objects.filter(piece_type_name=str(piece_types[i].piece_type_name)),
    piece_genre         = Genre.objects.filter(genre_name=str(piece_genres[0].genre_name)),
    piece_name          = piece_name[i],
    piece_description   = piece_description[i],

        prompt_piece.save()
        to_return.append(prompt_piece)
        )'''

    return to_return
