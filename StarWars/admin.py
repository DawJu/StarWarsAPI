from django.contrib import admin

from StarWars.models import Character, Movie, CharacterMovie

# Register your models here.

admin.site.register(Character)
admin.site.register(Movie)
admin.site.register(CharacterMovie)
