import pytest
from django.contrib.auth.models import User


@pytest.mark.django_db
def test_create_user():
    User.objects.create_user('test','test@test.com','test')
    count = User.objects.all().count()
    assert count== 1 
    