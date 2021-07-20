from rest_framework import serializers
from .models import Category, Thing


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"
        # fields = (
        #     "_id",
        #     #"id",
        #     "name",
        #     "slug",
        #     "created_at",
        #     "updated_at",
        #     "create_by_id",
        #     "update_by_id",
        # )


class ThingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Thing
        fields = "__all__"

        # fields = (
        #     "_id",
        #     "category",
        #     "owner",
        #     "title",
        #     "image",
        #     "content",
        #     "slug",
        #     "status",
        # )
