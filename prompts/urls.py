from django.conf.urls import url

from .views import GenreList

urlpatterns = [
    # For genres
    url(r'^$', GenreList.as_view(), name='genres-list')

    # Something else
]
