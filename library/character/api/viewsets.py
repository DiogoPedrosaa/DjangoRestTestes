from rest_framework import viewsets
from character.api import serializer
from character import models

class CharacterViewSet(viewsets.ModelViewSet):
    serializer_class = serializer.CharactersSerializer
    queryset = models.Character.objects.all()