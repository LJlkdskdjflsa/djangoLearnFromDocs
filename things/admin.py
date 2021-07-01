from django.contrib import admin
from . import models


@admin.register(models.Thing)
class OwnerAdmin(admin.ModelAdmin):
    list_display = ("pk", "category", "owner", "title", "content", "slug", "status")
    prepopulated_fields = {
        "slug": ("title",),
    }


admin.site.register(models.Category)
