import pytest
from django.contrib.auth.models import User

@pytest.fixture()
def user_1(db):
    return User.objects.create_user('test_user')