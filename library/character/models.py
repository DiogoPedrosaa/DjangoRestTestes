from django.db import models
from uuid import uuid4
from django.utils.text import slugify


class Tags(models.Model):
   name = models.CharField(max_length=255)
   slug = models.SlugField(unique = True)

   def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Tags, self).save(*args, **kwargs)

   def __str__(self):
      return self.name
   

class Character(models.Model):
   CLASS_CHOICES = [
        ('Black Guard', 'Black Guard'),
        ('Arcanist', 'Arcanist'),
        ('Fighter', 'Fighter'),
        ('Bardo', 'Bardo'),
        ('SoulBow', 'SoulBow'),
    ]
   id_char =  models.UUIDField(primary_key=True, default=uuid4, editable=False)
   char_nick = models.CharField(max_length= 225)
   char_legacy_level = models.IntegerField()
   char_effect_level = models.IntegerField()
   char_class = models.CharField(max_length=50, choices=CLASS_CHOICES)
   char_build = models.URLField(blank=True, null=True)
   tags = models.ManyToManyField(Tags)

   def __str__(self):
        return self.char_nick




   


   