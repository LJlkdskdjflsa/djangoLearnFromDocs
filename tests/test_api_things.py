from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from things.models import Thing, Category
from users.models import User


class ThingAPITest(APITestCase):
    def test_view_things(self):
        url = reverse("things:list-create")
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_things(self):
        self.test_category_1 = Category.objects.create(name="test_category_1")
        self.test_user_1 = User.objects.create(
            username="test_user_1",
            password="password",
        )
        data = {
            "category_id": 1,
            "title": "test_thing_1",
            "owner_id": 1,
            "content": "test_thing_1 content",
            "slug": "thing-testthing1",
            "status": "using",
        }

        url = reverse("things:list-create")
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
