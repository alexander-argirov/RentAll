from django.urls import reverse
from django.test import TestCase

from RentAll.accounts.models import RentAllUser, Profile


class ProfileUpdateViewTestCase(TestCase):
    def setUp(self):
        self.user = RentAllUser.objects.create_user(email='test@example.com', password='testpassword')
        try:
            self.profile = Profile.objects.get(user=self.user)
            self.profile.delete()
        except Profile.DoesNotExist:
            pass
        self.profile = Profile.objects.create(user=self.user, first_name='Test', last_name='User',
                                              date_of_birth='1990-01-01', phone_number='0888888887')

    def test_update_profile_with_valid_data(self):
        self.client.login(email='test@example.com', password='testpassword')
        data = {
            'first_name': 'Updated',
            'last_name': 'Profile',
            'date_of_birth': '1995-05-05',
            'phone_number': '0888888888',
        }
        response = self.client.post(reverse('edit profile', kwargs={'pk': self.profile.pk}), data)
        self.assertEqual(response.status_code, 302)  # Check for redirect
        updated_profile = Profile.objects.get(pk=self.profile.pk)
        self.assertEqual(updated_profile.first_name, 'Updated')
        self.assertEqual(updated_profile.last_name, 'Profile')
        self.assertEqual(str(updated_profile.date_of_birth), '1995-05-05')
        self.assertEqual(updated_profile.phone_number, '0888888888')

    def test_update_profile_with_invalid_data(self):
        self.client.login(email='test@example.com', password='testpassword')
        data = {
            'first_name': '',  # Invalid data
            'last_name': 'Profile',
            'date_of_birth': '1995-05-05',
            'phone_number': '0888888888',
        }
        response = self.client.post(reverse('edit profile', kwargs={'pk': self.profile.pk}), data)
        self.assertEqual(response.status_code, 302)  # Check for redirect
        self.assertRedirects(response,
                             reverse('detail profile', kwargs={'pk': self.profile.pk}))

    def test_redirect_after_update_profile(self):
        self.client.login(email='test@example.com', password='testpassword')
        data = {
            'first_name': 'Updated',
            'last_name': 'Profile',
            'date_of_birth': '1995-05-05',
            'phone_number': '0888888888',
        }
        response = self.client.post(reverse('edit profile', kwargs={'pk': self.profile.pk}), data)
        updated_profile = Profile.objects.get(pk=self.profile.pk)
        self.assertEqual(updated_profile.first_name, 'Updated')
        self.assertEqual(updated_profile.last_name, 'Profile')
        self.assertEqual(str(updated_profile.date_of_birth), '1995-05-05')
        self.assertEqual(updated_profile.phone_number, '0888888888')