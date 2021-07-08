# from djongo import models
from users.models import User
from django.db import models
from helpers.models import TrackingModel

# from django.contrib.auth.models import User
from django.conf import settings
from django.utils.translation import gettext_lazy as _

# the location to upload file
def upload_to(instance, filename):
    return "things/{filename}".format(filename=filename)


class Category(TrackingModel):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=250, unique=True)
    parent = models.ForeignKey(
        "self", null=True, blank=True, on_delete=models.SET_NULL, default=None
    )

    def __str__(self):
        return self.name


class Thing(TrackingModel):
    options = (
        ("planing", "Planing"),
        ("making", "Making"),
        ("using", "Using"),
        ("broken", "Broken"),
    )
    category = models.ForeignKey(
        Category, null=True, blank=True, on_delete=models.PROTECT, default=1
    )
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        verbose_name="擁有者",
        related_name="%(class)s_owner",
    )
    title = models.CharField(max_length=250)
    content = models.TextField(null=True)
    slug = models.SlugField(max_length=250, unique=True)
    image = models.FileField(
        _("Image"), upload_to=upload_to, default="things/default.jpeg"
    )
    status = models.CharField(max_length=50, choices=options, default="using")
