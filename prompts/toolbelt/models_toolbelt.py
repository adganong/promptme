from django.db                  import models
from django.conf                import settings
from django.urls                import reverse
from rest_framework.reverse     import reverse as api_reverse
from prompts.models import Genre, PromptPiece, BuiltPrompt, PieceType


def make_prompt_based_on_genre(genre_id):
    pass


#
def make_wild_card_prompt():
    pass


# This takes in the piece I want, and also the genre I want, but genre is not needed.
def get_specific_piece_based_on_genre(piece_id, genre_id = None):
    pass


def get_specific_piece_general(piece):
    pass
