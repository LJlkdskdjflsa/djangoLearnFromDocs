import pytest


@pytest.mark.django_db
def test_create_user(user_1):
    user_1.set_password("new-password")
    assert user_1.check_password("new-password") is True
    