from rest_framework import serializers
from .models import Category, Thing


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category

        fields = (
            # "_id",
            "id",
            "name",
            "created_at",
            "updated_at",
            "create_by_id",
            "update_by_id",
        )


class ThingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Thing
        fields = ("pk", "category", "owner", "title", "content", "slug", "status")
