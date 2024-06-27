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
        ('Apothecary', 'Apothecary'),
        ('Archivist', 'Archivist'),
        ('Astral Ranger', 'Astral Ranger'),
        ('Battlemage', 'Battlemage'),
        ('Bloodthrall', 'Bloodthrall'),
        ('Boneweaver', 'Boneweaver'),
        ('Cabalist', 'Cabalist'),
        ('Cleric', 'Cleric'),
        ('Confessor', 'Confessor'),
        ('Crusader', 'Crusader'),
        ('Dark Knight', 'Dark Knight'),
        ('Death Warden', 'Death Warden'),
        ('Dreadknight', 'Dreadknight'),
        ('Eldritch', 'Eldritch'),
        ('Emissary', 'Emissary'),
        ('Executioner', 'Executioner'),
        ('Herald', 'Herald'),
        ('Hex Blade', 'Hex Blade'),
        ('Hex Mage', 'Hex Mage'),
        ('Hex Ranger', 'Hex Ranger'),
        ('Hex Warden', 'Hex Warden'),
        ('Inquisitive', 'Inquisitive'),
        ('Justicar', 'Justicar'),
        ('Loremaster', 'Loremaster'),
        ('Magus', 'Magus'),
        ('Marshal', 'Marshal'),
        ('Minstrel', 'Minstrel'),
        ('Necromancer', 'Necromancer'),
        ('Nightblade', 'Nightblade'),
        ('Occultist', 'Occultist'),
        ('Oracle', 'Oracle'),
        ('Paladin', 'Paladin'),
        ('Paragon', 'Paragon'),
        ('Planeswalker', 'Planeswalker'),
        ('Reaver', 'Reaver'),
        ('Runesmith', 'Runesmith'),
        ('Sage', 'Sage'),
        ('Scholar', 'Scholar'),
        ('Sentinel', 'Sentinel'),
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




   


   