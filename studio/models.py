from django_countries.fields import CountryField
from multiselectfield import MultiSelectField
from django.db import models


PRODUCT_TYPES = (
        ("Movie", "Movie"),
        ("Short", "Shorts"),
        ("Series", "Series"),
        ("Cartoon", "Cartoons"),
        ("Anime", "Animes"),
        ("Music", "Musics"),
        ("Premier", "Premiers"),
    )
# Create your models here.
class Studio(models.Model):
    name = models.CharField(max_length=255)
    founder_name = models.CharField(max_length=255)
    location = CountryField()
    product_types = MultiSelectField(choices=PRODUCT_TYPES, max_length=200)
    employee_count = models.IntegerField(default=1)
    profit = models.CharField(max_length=255)
    capital = models.CharField(max_length=255)
    page = models.CharField(max_length=255)
    history = models.TextField()
    video = models.FileField(upload_to="media/studio/video/%Y/%m/%d", null=True, blank=True)
    logo = models.ImageField(upload_to="images/studio/logo/", null=True, blank=True)
    award = models.CharField(max_length=255, null=True, blank=True)
    news = models.ForeignKey("news.News", on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = "Studio"
        verbose_name_plural = "Studios"
        indexes = [models.Index(fields=["name"])]