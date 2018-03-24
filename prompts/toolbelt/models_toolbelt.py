from django.db                  import models
from django.conf                import settings
from django.urls                import reverse
from rest_framework.reverse     import reverse as api_reverse
from prompts.models import Genre, PromptPiece, BuiltPrompt, PieceType


# This takes in the piece I want, and also the genre I want, but genre is not needed.
def get_random_piece_based_on_genre_and_type(genre_id, type_id):
    return PromptPiece.objects.filter(piece_type=type_id, piece_genre=genre_id)


def get_specific_piece_general(piece):
    pass


def make_random_prompt(genre_id=None):
    if genre_id is None:
        print("Me first")
        return BuiltPrompt.objects.create(
            prompt_name='new prompt',
            is_wild_card=True,
            genre=None,
            prompt_person=PromptPiece.randomPieceBy.type(1)[0],
            prompt_place=PromptPiece.randomPieceBy.type(2)[0],
            prompt_thing=PromptPiece.randomPieceBy.type(3)[0],
            prompt_scenario=PromptPiece.randomPieceBy.type(4)[0],
        )
    else:
        print("Me Second")
        return BuiltPrompt.objects.create(
            prompt_name='new prompt',
            is_wild_card=False,
            genre=Genre.objects.get(pk=genre_id),
            prompt_person=PromptPiece.randomPieceBy.genre_and_type(genre_id, 1)[0],
            prompt_place=PromptPiece.randomPieceBy.genre_and_type(genre_id, 2)[0],
            prompt_thing=PromptPiece.randomPieceBy.genre_and_type(genre_id, 3)[0],
            prompt_scenario=PromptPiece.randomPieceBy.genre_and_type(genre_id, 4)[0],
        )



