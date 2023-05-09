from django.contrib.auth.models import Group
from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Category)
admin.site.register(Studio)
admin.site.register(Movie)
admin.site.register(Image)
admin.site.register(Genre)


admin.site.unregister(Group)
