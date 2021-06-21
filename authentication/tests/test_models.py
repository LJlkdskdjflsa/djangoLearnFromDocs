from rest_framework.test import APITestCase
from authentication.models import User


class TestModel(APITestCase):
    def test_creates_user(self):
        user = User.objects.create_user("test_user", "test@test.com", "test_password")
        self.assertIsInstance(user, User)
        self.assertFalse(user.is_staff)
        self.assertEqual(user.email, "test@test.com")

    def test_creates_super_user(self):
        user = User.objects.create_superuser(username="test_user", email="test@test.com", password="test_password")
        self.assertIsInstance(user, User)
        self.assertTrue(user.is_staff)
        self.assertEqual(user.email, "test@test.com")

    def test_raises_error_when_no_username_is_supplied(self):
        self.assertRaises(
            ValueError, User.objects.create_user, username="", email="test@test.com", password="test_password"
        )

    def test_raises_error_with_message_when_no_username_is_supplied(self):
        with self.assertRaisesMessage(ValueError, "The given username must be set"):
            User.objects.create_user(username="", email="test@test.com", password="test_password")

    def test_raises_error_when_no_email_is_supplied(self):
        self.assertRaises(
            ValueError, User.objects.create_user, username="testuser", email="", password="test_password"
        )

    def test_raises_error_with_message_when_no_email_is_supplied(self):
        with self.assertRaisesMessage(ValueError, "The given email must be set"):
            User.objects.create_user(username="testuser", email="", password="test_password")


"""    def test_super_user_with_staff_status(self):
        with self.assertRaisesMessage(ValueError, 'Superuser must have is_staff=True.'):
            User.objects.create_superuser(username='testsuperuser', email='testsuperuser@test.com', password='test_password',is_staff=False)

    def test_super_user_with_super_user_status(self):
        with self.assertRaisesMessage(ValueError, 'Superuser must have is_superuser=True.'):
            User.objects.create_superuser(username='testsuperuser', email='testsuperuser@test.com', password='test_password',is_superuser=False)"""
