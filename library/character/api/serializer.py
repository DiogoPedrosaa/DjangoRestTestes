from rest_framework import serializers
from character import models

class CharactersSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Character
        fields = '__all__'