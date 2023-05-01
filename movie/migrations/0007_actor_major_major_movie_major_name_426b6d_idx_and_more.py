# Generated by Django 4.2 on 2023-05-01 18:05

from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0006_remove_movie_category_remove_movie_studio_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('brief_info', models.CharField(max_length=300)),
                ('birth_place', models.CharField(max_length=255)),
                ('citizenship', django_countries.fields.CountryField(max_length=2)),
                ('career', models.CharField(max_length=50)),
                ('information', models.TextField()),
            ],
            options={
                'verbose_name': 'Actor',
                'verbose_name_plural': 'Actor',
            },
        ),
        migrations.CreateModel(
            name='Major',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
            ],
            options={
                'verbose_name': 'Major',
                'verbose_name_plural': 'Majors',
            },
        ),
        migrations.AddIndex(
            model_name='major',
            index=models.Index(fields=['name'], name='movie_major_name_426b6d_idx'),
        ),
        migrations.AddField(
            model_name='actor',
            name='genre',
            field=models.ManyToManyField(to='movie.genre'),
        ),
        migrations.AddField(
            model_name='actor',
            name='status',
            field=models.ManyToManyField(to='movie.major'),
        ),
        migrations.AddField(
            model_name='image',
            name='actor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='movie.actor'),
        ),
        migrations.AddIndex(
            model_name='actor',
            index=models.Index(fields=['name'], name='movie_actor_name_5e0ddc_idx'),
        ),
    ]