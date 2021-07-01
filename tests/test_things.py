import pytest
from django.test import TestCase
from users.models import User
from things.models import Thing, Category


class TestCreateThing(TestCase):
    @classmethod
    def setUpTestData(cls):
        test_category_1 = Category.objects.create(name="test_category_1")
        test_user_1 = User.objects.create(
            username="test_user_1",
            password="password",
        )
        test_thing_1 = Thing.objects.create(
            category_id=1,
            title="test_thing_1",
            owner_id=1,
            content="test_thing_1 content",
            slug="thing-testthing1",
            status="using",
        )

    def test_thing_content(self):
        thing = Thing.objects.get(id=1)
        category = Category.objects.get(id=1)
        owner = f"{thing.owner}"
        title = f"{thing.title}"
        content = f"{thing.content}"
        status = f"{thing.status}"

        # check value
        self.assertEqual(owner, "test_user_1")
        self.assertEqual(title, "test_thing_1")
        self.assertEqual(content, "test_thing_1 content")
        self.assertEqual(status, "using")
        # self.assertEqual(str(thing), "test_thing_1")
        self.assertEqual(str(category), "test_category_1")
