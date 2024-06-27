from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from character.api.serializer import CharactersSerializer
from character.models import Character, Tags
from rest_framework.parsers import JSONParser

class CharacterViewSet(viewsets.ModelViewSet):
    serializer_class = CharactersSerializer
    queryset = Character.objects.all()

    @action(detail=False, methods=['get'], url_path='search-by-nick')
    def get_by_nick(self, request):
        nick = request.query_params.get('nick', None)
        if nick is not None:
            character = get_object_or_404(Character, char_nick=nick)
            serializer = self.get_serializer(character)
            return Response(serializer.data)
        return Response({'error': 'Nick parameter is required'}, status=status.HTTP_400_BAD_REQUEST)
    

    

    @action(detail=False, methods=['get'], url_path='search-by-class')
    def get_by_class(self, request):
        char_class = request.query_params.get('class', None)
        if char_class is not None:
            characters = Character.objects.filter(char_class=char_class)
            if characters.exists():
                serializer = self.get_serializer(characters, many=True)
                return Response(serializer.data)
            else:
                return Response({'error': 'No characters found for this class'}, status=status.HTTP_404_NOT_FOUND)
        return Response({'error': 'Class parameter is required'}, status=status.HTTP_400_BAD_REQUEST)



    
    @action(detail=False, methods=['get'], url_path='search-by-tag')
    def get_by_tag(self, request):
        tag_name = request.query_params.get('tag', None)
        if tag_name is not None:
            tag = get_object_or_404(Tags, name=tag_name)
            characters = Character.objects.filter(tags=tag)
            if characters.exists():
                serializer = self.get_serializer(characters, many=True)
                return Response(serializer.data)
            else:
                return Response({'error': 'No characters found for this tag'}, status=status.HTTP_404_NOT_FOUND)
        return Response({'error': 'Tag parameter is required'}, status=status.HTTP_400_BAD_REQUEST)
    

    @action(detail=False, methods=['get'], url_path='search-by-tag-id')
    def get_by_tag_id(self, request):
        tag_id = request.query_params.get('tag', None)
        if tag_id is not None:
            tag = get_object_or_404(Tags, id=tag_id)
            characters = Character.objects.filter(tags=tag)
            if characters.exists():
                serializer = self.get_serializer(characters, many=True)
                return Response(serializer.data)
            else:
                return Response({'error': 'No characters found for this tag'}, status=status.HTTP_404_NOT_FOUND)
        return Response({'error': 'Tag parameter is required'}, status=status.HTTP_400_BAD_REQUEST)
    


    @action(detail=False, methods=['get'], url_path='search-by-legacy')
    def get_by_legacy(self, request):
        legacy = request.query_params.get('legacy', None)
        if legacy is not None:
            characters = Character.objects.filter(char_legacy_level=legacy)
            if characters.exists():
                serializer = self.get_serializer(characters, many = True)
                return Response(serializer.data)
            else:
                return Response({'error': 'No characters found for this legacy level'}, status=status.HTTP_404_NOT_FOUND)
        return Response({'error': 'Legacy Level parameter is required'}, status=status.HTTP_400_BAD_REQUEST)
    


    @action(detail=False, methods=['get'], url_path='search-by-effect')
    def get_by_effect(self, request):
        effect = request.query_params.get('effect', None)
        if effect is not None:
            characters = Character.objects.filter(char_effect_level=effect)
            if characters.exists():
                serializer = self.get_serializer(characters, many = True)
                return Response(serializer.data)
            else:
                return Response({'error': 'No characters found for this effectiviness level'}, status=status.HTTP_404_NOT_FOUND)
        return Response({'error': 'Effectiviness Level parameter is required'}, status=status.HTTP_400_BAD_REQUEST)
    

    @action(detail=True, methods=['put'], url_path='update-character')
    def update_character(self, request, pk=None):
        character = get_object_or_404(Character, pk=pk)
        data = JSONParser().parse(request)
        serializer = self.get_serializer(character, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
