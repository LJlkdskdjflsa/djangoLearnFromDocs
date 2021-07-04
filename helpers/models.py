# from djongo import models
from django.db import models

# from django.contrib.auth.models import User
from users.models import User
from django.conf import settings


class TrackingModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    create_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        verbose_name="创建人",
        related_name="%(class)s_create_by",
    )

    update_by = models.ForeignKey(
        User,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        verbose_name="最后编辑人",
        related_name="%(class)s_update_by",
    )

    class Meta:
        abstract = True
        # set the model be abstract
        ordering = ("-created_at",)
