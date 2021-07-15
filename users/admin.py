from django.contrib import admin
from users.models import User
from django.contrib.auth.admin import UserAdmin
from django.forms import TextInput, Textarea, CharField
from django import forms
from django.db import models


from django.contrib import admin
from . import models

# user admin site
# write custom adin site
class UserAdminArea(admin.AdminSite):
    site_header = "User Admin area"


user_site = UserAdminArea(name="UserAdmin")

# register to default admin
class UserAdminConfig(UserAdmin):
    model = User
    search_fields = (
        "email",
        "username",
    )
    list_filter = ("email", "username", "is_active", "is_staff")
    ordering = ("-start_date",)
    list_display = ("email", "username", "is_active", "is_staff")
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "email",
                    "username",
                )
            },
        ),
        ("Permissions", {"fields": ("is_staff", "is_active")}),
        ("Personal", {"fields": ("about",)}),
    )
    # AttributeError: module 'users.models' has no attribute 'TextField' ?
    # formfield_overrides = {
    #     models.TextField: {"widget": Textarea(attrs={"rows": 20, "cols": 60})},
    # }
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "username",
                    "password1",
                    "password2",
                    "is_active",
                    "is_staff",
                ),
            },
        ),
    )


admin.site.register(User, UserAdminConfig)
