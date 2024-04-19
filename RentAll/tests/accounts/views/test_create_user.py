from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import TestCase
from django.test.client import Client


class TestRegisterUserView(TestCase):
    def setUp(self):
        self.client = Client()

    def test_redirect_after_register(self):
        data = {
            'email': 'test@example.com',
            'password1': 'testpassword',
            'password2': 'testpassword',
        }
        response = self.client.post(reverse('register user'), data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('edit profile', kwargs={'pk': get_user_model().objects.get(email='test@example.com').pk}))

    def test_invalid_register_data(self):
        data = {
            'email': 'invalid_email',
            'password1': 'testpassword',
            'password2': 'testpassword123',
        }
        response = self.client.post(reverse('register user'), data)
        self.assertEqual(response.status_code, 200)

    def test_login_after_register(self):
        data = {
            'email': 'test@example.com',
            'password1': 'testpassword',
            'password2': 'testpassword',
        }
        response = self.client.post(reverse('register user'), data, follow=True)
        self.assertTrue(response.context['user'].is_authenticated)

    def test_profile_associated_with_user(self):
        data = {
            'email': 'test@example.com',
            'password1': 'testpassword',
            'password2': 'testpassword',
        }
        response = self.client.post(reverse('register user'), data)
        user = get_user_model().objects.get(email='test@example.com')
        self.assertIsNotNone(user.profile)



