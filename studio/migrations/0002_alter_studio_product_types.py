# Generated by Django 4.2 on 2023-05-08 10:16

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('studio', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studio',
            name='product_types',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Movie', 'Movie'), ('Short', 'Shorts'), ('Series', 'Series'), ('Cartoon', 'Cartoons'), ('Anime', 'Animes'), ('Music', 'Musics'), ('Premier', 'Premiers')], max_length=200),
        ),
    ]