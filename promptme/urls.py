from django.conf.urls import url, include
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns
from prompts import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # For genres
    url(r'^api/genres', include('prompts.urls', namespace='api-genres')),
]

urlpatterns = format_suffix_patterns(urlpatterns)
