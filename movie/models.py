from django.db import models
from django_countries.fields import CountryField
from django.template.defaultfilters import slugify
from multiselectfield import MultiSelectField

RATING_CHOICES = (
    ("5", "5"),
    ("4", "4"),
    ("3", "3"),
    ("2", "2"),
    ("1", "1"),
)


class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = "Tag"
        verbose_name_plural = "Tags"
        indexes = [models.Index(fields=["name"])]


class News(models.Model):
    title = models.CharField(max_length=255)
    contnent = models.TextField()
    publication_date = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    source = models.CharField(max_length=255)
    tag = models.ManyToManyField(Tag)

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = "News"
        verbose_name_plural = "News"
        indexes = [models.Index(fields=["title"])]


class Genre(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = "Genre"
        verbose_name_plural = "Genres"
        indexes = [models.Index(fields=["name"])]


class Category(models.Model):
    image = models.ImageField(upload_to="images/category/logo/")
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        indexes = [models.Index(fields=["name"])]


class Studio(models.Model):
    PRODUCT_TYPES = (
        ("Movie", "Movie"),
        ("Short", "Shorts"),
        ("Series", "Series"),
        ("Cartoon", "Cartoons"),
        ("Anime", "Animes"),
        ("Music", "Musics"),
        ("Premier", "Premiers"),
    )
    name = models.CharField(max_length=255)
    founder_name = models.CharField(max_length=255)
    location = CountryField()
    product_types = MultiSelectField(choices=PRODUCT_TYPES, max_length=7)
    employee_count = models.IntegerField(default=1)
    profit = models.CharField(max_length=255)
    capital = models.CharField(max_length=255)
    page = models.CharField(max_length=255)
    history = models.TextField()
    video = models.FileField(upload_to="media/studio/video/%Y/%m/%d", null=True)
    logo = models.ImageField(upload_to="images/studio/logo/", null=True)
    award = models.CharField(max_length=255, null=True, blank=True)
    news = models.ForeignKey(News, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = "Studio"
        verbose_name_plural = "Studios"
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
    cast = models.CharField(max_length=256)
    brief_information = models.TextField()
    genre = models.ManyToManyField(Genre)
    trailer = models.FileField(upload_to="media/movie/trailes/")
    logo = models.ImageField(upload_to="images/movie/logo/%d")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    age_limit = models.IntegerField(default=1)
    category = models.ManyToManyField(Category)
    studio = models.ManyToManyField(Studio)
    tag = models.ManyToManyField(Tag)

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
    else:
        return f"images/other/%Y/%m/%d/{filename}"


class Image(models.Model):
    image = models.ImageField(upload_to=get_image_upload_path)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, null=True, blank=True)
    news = models.ForeignKey(News, on_delete=models.CASCADE, null=True, blank=True)
    studio = models.ForeignKey(Studio, on_delete=models.CASCADE, null=True, blank=True)
