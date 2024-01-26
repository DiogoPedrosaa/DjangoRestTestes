from django.db import models
from uuid import uuid4


class Character(models.Model):
   id_char =  models.UUIDField(primary_key=True, default=uuid4, editable=False)
   char_nick = models.CharField(max_length= 225)
   char_legacy_level = models.IntegerField()
   char_effect_level = models.IntegerField()
   char_class = models.CharField(max_length= 50)
   char_guild = models.CharField(max_length= 50)
   char_build = models.URLField(blank=True, null=True)
   