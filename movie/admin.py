from django.contrib import admin
from .models import *
from django.contrib.auth.models import Group
# Register your models here.
admin.site.register(Movie)
admin.site.register(Tag)
admin.site.register(Image)
admin.site.register(Studio)
admin.site.register(Category)
admin.site.register(Genre)
admin.site.register(News)
admin.site.unregister(Group)