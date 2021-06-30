from django.test import TestCase
from django.contrib.auth import get_user_model

class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """Test Create New User With Email is successful"""
        email = "daniyal.ahmed.177@gmail.com"
        password = "1234657"
        user = get_user_model().objects.create_user(
            email = email,
            password = password
        )
        self.assertEqual(user.email,email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test the email for a new user is normalized"""
        email = "daniyal.ahmed.177@GMAIL.com"
        user = get_user_model().objects.create_user(email, '123456')
        self.assertEqual(user.email,email.lower())

    def test_new_user_invalid_email(self):
        """Test  user with no email"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test123')

    def test_create_new_superuser(self):
        """Test the email for a new user is normalized"""
        email = "daniyal.ahmed.177@GMAIL.com"
        user = get_user_model().objects.create_superuser(email, '123456')
        self.assertEqual(user.email,email.lower())
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
