# Generated by Django 4.2 on 2023-05-01 18:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0007_actor_major_major_movie_major_name_426b6d_idx_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='actor',
            options={'verbose_name': 'Actor', 'verbose_name_plural': 'Actors'},
        ),
    ]