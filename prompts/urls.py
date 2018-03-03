from django.conf.urls import url

from .views import GenreList, PieceTypeList, PromptPieceList, BuiltPromptList

urlpatterns = [
    # For genres
    url(r'^$', GenreList.as_view(), name='genres-list'),
    url(r'^$', PieceTypeList.as_view(), name='piece_types-list'),
    # This probably won't ever be used? Need to make one that can directly access certain pieces
    url(r'^$', PromptPieceList.as_view(), name='prompt_pieces-list'),
    url(r'^$', BuiltPromptList.as_view(), name='built_prompts-list'),
    # Something else
]

