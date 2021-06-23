import pytest


@pytest.mark.django_db
def test_create_user(new_user1):
    new_user1.set_password("new-password")
    # assert user_1.check_password("new-password") is True


def test_new_user(new_user1):
    print(new_user1.first_name)
    # assert new_user.first_name == "firstname"
