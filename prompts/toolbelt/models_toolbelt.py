from django.db                  import models
from django.conf                import settings
from django.urls                import reverse
from rest_framework.reverse     import reverse as api_reverse
from prompts.models import Genre, PromptPiece, BuiltPrompt, PieceType


# This takes in the piece I want, and also the genre I want, but genre is not needed.
def get_specific_piece_based_on_genre_and_type(genre_id, type_id):
    qs = PromptPiece.objects.filter(piece_type=type_id, piece_genre=genre_id)
    return qs


def get_specific_piece_general(piece):
    pass


def make_prompt_based_on_genre(genre_id):
    pass



def make_wild_card_prompt():
    pass


