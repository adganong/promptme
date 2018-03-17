from django.db                  import models
from django.conf                import settings
from django.urls                import reverse
from rest_framework.reverse     import reverse as api_reverse
from prompts.models import Genre, PromptPiece, BuiltPrompt, PieceType


# This takes in the piece I want, and also the genre I want, but genre is not needed.
def get_piece_based_on_genre_and_type(genre_id, type_id):
    return PromptPiece.objects.filter(piece_type=type_id, piece_genre=genre_id)


def get_specific_piece_general(piece):
    pass


def make_prompt_based_on_genre(genre_id):
    person = get_piece_based_on_genre_and_type(genre_id, 1)
    place = get_piece_based_on_genre_and_type(genre_id, 2)
    thing = get_piece_based_on_genre_and_type(genre_id, 3)
    scenario = get_piece_based_on_genre_and_type(genre_id, 4)




def make_wild_card_prompt():
    pass


