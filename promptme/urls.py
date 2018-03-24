from django.conf.urls import url, include
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns
from prompts import views

# Main URLS redirect
# All aboard!
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # For genres
    # Actually, turns out most of these are redundant. that's okay
    url(r'^api/prompts/', include('prompts.urls', namespace='api-genres')),
]

urlpatterns = format_suffix_patterns(urlpatterns)
