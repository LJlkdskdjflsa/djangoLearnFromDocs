from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from things.models import Thing, Category

from users.models import User

# from django.contrib.auth.models import User


class ThingAPITest(APITestCase):
    def test_view_things(self):
        url = reverse("things:list-create")
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_things(self):
        self.test_category_1 = Category.objects.create(name="test_category_1")
        self.test_user_1 = User.objects.create_superuser(
            username="test_user_1",
            password="password",
        )
        print(self.test_user_1.id)
        print(self.test_category_1.id)

        data = {
            "category": 1,
            "owner": 1,
            "title": "adfg",
            "content": "asdf",
            "slug": "asdf",
            "status": "using",
        }

        url = reverse("things:list-create")
        client = APIClient()
        client.login(username=self.test_user_1.username, password="password")
        response = self.client.post(url, data, format="json")
        print(response)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_thing_update(self):
        client = APIClient()
        self.test_category_1 = Category.objects.create(name="test_category_1")
        self.test_user_1 = User.objects.create_superuser(
            username="test_user_1",
            password="password",
        )
        self.test_thing_1 = Thing.objects.create(
            category_id=1,
            title="test_thing_1",
            owner_id=1,
            content="test_thing_1 content",
            slug="thing-testthing1",
            status="using",
        )
        client.login(username=self.test_user_1.username, password="password")
        url = reverse(("things:detail-create"), kwargs={"pk": 1})

        data = {
            "category": 1,
            "owner": 1,
            "title": "adfg",
            "content": "asdf",
            "slug": "asdf",
            "status": "using",
        }
        response = client.put(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
