from django.shortcuts import render

from django.shortcuts import render
from character.api.viewsets import CharacterViewSet

def character_list(request):
    characters = CharacterViewSet().get_queryset()
    return render(request, 'character_list.html', {'characters': characters})