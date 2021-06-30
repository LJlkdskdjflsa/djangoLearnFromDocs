from rest_framework import serializers
from .models import Category, Thing


class ThingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Thing
        fields = ("pk", "category", "owner", "title", "content", "slug", "status")
