from django.conf.urls import url

from .views import \
    GenreList, PieceTypeList, PromptPieceList, BuiltPromptList, GetPromptByType, \
    GetRandomPrompt, GetWildcardPrompt

urlpatterns = [
    # For genres
    url(r'^genres_list/', GenreList.as_view(), name='genres-list'),
    url(r'^piece_types_list/', PieceTypeList.as_view(), name='piece_types-list'),
    # This probably won't ever be used? Need to make one that can directly access certain pieces
    url(r'^prompt_pieces_list/', PromptPieceList.as_view(), name='prompt_pieces-list'),
    url(r'^built_prompts_list/', BuiltPromptList.as_view(), name='built_prompts-list'),
    url(r'^get_piece/$', GetPromptByType.as_view(), name='prompt_pieces-rud'),
    url(r'^get_random_prompt/$', GetRandomPrompt.as_view(), name='prompt_pieces-rud'),
    url(r'^get_wild_card_prompt/', GetWildcardPrompt.as_view(), name='prompt_pieces-rud'),
    #url(r'^test/$', GetPromptByType.as_view(), name='prompt_pieces-rud'),
]

