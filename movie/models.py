from django.template.defaultfilters import slugify
from django_countries.fields import CountryField
from studio.models import Studio
from django.db import models

RATING_CHOICES = (
    ("5", "5"),
    ("4", "4"),
    ("3", "3"),
    ("2", "2"),
    ("1", "1"),
)

class Genre(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = "Genre"
        verbose_name_plural = "Genres"
        indexes = [models.Index(fields=["name"])]


class Category(models.Model):
    # image = models.ImageField(upload_to="images/category/logo/")
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        indexes = [models.Index(fields=["name"])]


class Movie(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(null=True, blank=True, unique=True)
    production_year = models.DateField()
    country = CountryField(multiple=True)
    screenwriter = models.CharField(max_length=255)
    producer = models.CharField(max_length=255)
    producer = models.CharField(max_length=255)
    composer = models.CharField(max_length=255)
    artist = models.CharField(max_length=255)
    montage = models.CharField(max_length=255)
    world_premier_date = models.DateField()
    world_rating = models.CharField(max_length=20, choices=RATING_CHOICES, default=2)
    duration = models.IntegerField(default=0)
    cast = models.ManyToManyField('actor.Actor')
    brief_information = models.TextField()
    genre = models.ManyToManyField(Genre)
    trailer = models.FileField(upload_to="media/movie/trailes/")
    logo = models.ImageField(upload_to="images/movie/logo/")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    age_limit = models.IntegerField(default=1)
    category = models.ManyToManyField(Category)
    studio = models.ManyToManyField(Studio)
    tag = models.ManyToManyField('news.Tag')

    def __str__(self) -> str:
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Movie"
        verbose_name_plural = "Movies"
        indexes = [models.Index(fields=["title"])]




def get_image_upload_path(instance, filename):
    if instance.movie:
        return f"images/movie/%Y/%m/%d/{instance.movie.id}/{filename}"
    elif instance.news:
        return f"images/news/%Y/%m/%d/{instance.news.id}/{filename}"
    elif instance.studio:
        return f"images/studio/%Y/%m/%d/{instance.studio.id}/{filename}"
    elif instance.actor:
        return f"images/actor/%Y/%m/%d/{instance.actor.id}/{filename}"
    else:
        return f"images/other/%Y/%m/%d/{filename}"


class Image(models.Model):
    image = models.ImageField(upload_to=get_image_upload_path)
    actor = models.ForeignKey('actor.Actor', on_delete=models.CASCADE, null=True, blank=True)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, null=True, blank=True)
    news = models.ForeignKey('news.News', on_delete=models.CASCADE, null=True, blank=True)
    studio = models.ForeignKey(Studio, on_delete=models.CASCADE, null=True, blank=True)
