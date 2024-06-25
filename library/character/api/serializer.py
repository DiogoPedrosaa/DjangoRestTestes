from rest_framework import serializers
from character.models import Tags, Character
from character import models

class TagsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tags
        fields = ['id', 'name', 'slug']

class CharactersSerializer(serializers.ModelSerializer):
    tags = TagsSerializer(many = True)
    class Meta:
        model = models.Character
        fields = [
            'id_char', 'char_nick', 'char_legacy_level', 'char_effect_level', 'char_class', 'char_build', 'tags'
        ]
