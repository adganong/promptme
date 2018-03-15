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
    url(r'^api/genres/', include('prompts.urls', namespace='api-genres')),
    url(r'^api/piece_types/', include('prompts.urls', namespace='api-piece_types')),
    url(r'^api/prompt_pieces/', include('prompts.urls', namespace='api-prompt_pieces')),
    url(r'^api/built_prompts/', include('prompts.urls', namespace='api-built_prompts')),
]

urlpatterns = format_suffix_patterns(urlpatterns)
