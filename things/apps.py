from django.apps import AppConfig
from django.contrib.admin.apps import AdminConfig

# write custome admin app
class ThingsAdminConfig(AdminConfig):
    default_site = "things.admin.ThingsAdminArea"


class ThingsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "things"
