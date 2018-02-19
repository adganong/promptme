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
