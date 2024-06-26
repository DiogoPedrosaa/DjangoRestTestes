# Generated by Django 5.0 on 2024-06-21 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('character', '0003_remove_character_char_guild'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='character',
            name='tags',
            field=models.ManyToManyField(to='character.tags'),
        ),
    ]
