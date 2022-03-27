from django.contrib import admin
from .models import Game, Review, Genre

admin.site.register(Genre)
admin.site.register(Game)
admin.site.register(Review)
