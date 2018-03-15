from django.conf.urls import url

from .views import GenreList, PieceTypeList, PromptPieceList, BuiltPromptList, PromptPieceRudView

urlpatterns = [
    # For genres
    url(r'^genres_list/', GenreList.as_view(), name='genres-list'),
    url(r'^piece_types_list/', PieceTypeList.as_view(), name='piece_types-list'),
    # This probably won't ever be used? Need to make one that can directly access certain pieces
    url(r'^prompt_pieces_list/', PromptPieceList.as_view(), name='prompt_pieces-list'),
    url(r'^built_prompts_list/', BuiltPromptList.as_view(), name='built_prompts-list'),
    # Something else
    url(r'^(?P<pk>\d+)/$', PromptPieceRudView.as_view(), name='prompt_pieces-rud'),
]

