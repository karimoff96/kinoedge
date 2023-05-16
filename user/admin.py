from django.contrib import admin
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin
from django.forms import Textarea, TextInput

# Register your models here.


class UserAdminConfig(UserAdmin):
    model = CustomUser
    search_fields = (
        "email",
        "user_name",
        "full_name",
        "password",
    )
    list_filter = ("email", "user_name", "full_name", "is_active", "is_staff", "is_verified")
    ordering = ("-start_date",)
    list_display = ("email", "user_name", "full_name", "is_active", "is_staff", "is_verified")
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "email",
                    "user_name",
                    "full_name",
                    "password",
                )
            },
        ),
        ("Permissions", {"fields": ("is_active", "is_staff", "is_verified")}),
        ("Personal", {"fields": ("about",)}),
    )
    formfield_overrides = {
        CustomUser.about: {'widget': Textarea(attrs={'rows':10, 'cols':40})},
    }
    add_fieldsets = (
        (None, {'classes': ('wide',),
                'fields':('email', 'user_name', 'full_name', 'password1', 'password2', 'is_active', 'is_staff', "is_verified")}
                ),
    )


admin.site.register(CustomUser, UserAdminConfig)
