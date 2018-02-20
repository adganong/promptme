from django.contrib import admin
from .models import Genre, PromptPiece, BuiltPrompt, PieceType
# Register your models here.

admin.site.register(Genre)
admin.site.register(PromptPiece)
admin.site.register(BuiltPrompt)
admin.site.register(PieceType)