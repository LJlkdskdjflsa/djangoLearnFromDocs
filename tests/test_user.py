import pytest
from users.models import User
from factories import UserFactory

user_factory = UserFactory


@pytest.mark.django_db
def test_create_user():
    User.objects.create_user("testqwe", "test@test.com", "testqwe")
    count = User.objects.all().count()
    assert count == 1


@pytest.mark.django_db
def test_new_user(user_factory):
    user = user_factory.create()
    count = User.objects.all().count()
    print(count)
    print(user.username)
    assert True
