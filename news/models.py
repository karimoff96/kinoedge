from django.db import models

# Create your models here.
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
    content = models.TextField()
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