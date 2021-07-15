from django.contrib import admin
from . import models

# things admin site
# write custom adin site
class ThingsAdminArea(admin.AdminSite):
    site_header = "Things Admin area"


things_site = ThingsAdminArea(name="ThingsAdmin")
things_site.register(models.Category)
things_site.register(models.Thing)


# default admin site
@admin.register(models.Thing)
class OwnerAdmin(admin.ModelAdmin):
    list_display = ("pk", "category", "owner", "title", "content", "slug", "status")
    prepopulated_fields = {
        "slug": ("title",),
    }


@admin.register(models.Category)
class OwnerAdmin(admin.ModelAdmin):
    list_display = ("_id", "name", "slug", "parent")
    prepopulated_fields = {
        "slug": ("name",),
    }


# register all models
import django.apps

# print out all models in the install app
models = django.apps.apps.get_models()
print(models)

# for model in models:
#     try:
#         admin.site.register(model)
#     except admin.sites.AlreadyRegistered:
#         pass
