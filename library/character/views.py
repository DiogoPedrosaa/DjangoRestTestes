from django.shortcuts import render

from django.shortcuts import render
from character.api.viewsets import CharacterViewSet
from character.models import Character

def character_list(request):
    characters = Character.objects.all()
    classes = Character.objects.values_list('char_class', flat=True).distinct()
    return render(request, 'characters/character_list.html', {'characters': characters, 'classes': classes})