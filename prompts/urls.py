from django.conf.urls import url

from .views import GenreList, PieceTypeList

urlpatterns = [
    # For genres
    url(r'^$', GenreList.as_view(), name='genres-list'),
    url(r'^$', PieceTypeList.as_view(), name='piece_types-list'),
    # Something else
]
