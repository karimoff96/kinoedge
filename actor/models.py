from django_countries.fields import CountryField
from django.db import models

# Create your models here.



class Major(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = "Major"
        verbose_name_plural = "Majors"
        indexes = [models.Index(fields=["name"])]


class Actor(models.Model):
    name = models.CharField(max_length=255)
    brief_info = models.CharField(max_length=300)
    birth_place = models.CharField(max_length=255)
    status = models.ManyToManyField(Major)
    citizenship = CountryField()
    career = models.CharField(max_length=50)
    genre = models.ManyToManyField('movie.Genre')
    information = models.TextField()

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = "Actor"
        verbose_name_plural = "Actors"
        indexes = [models.Index(fields=["name"])]

