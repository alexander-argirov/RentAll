from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group, Permission
from django.test import Client, TestCase
from django.urls import reverse


class TestArticleCreateView(TestCase):
    def setUp(self):
        self.client = Client()
        self.superuser = get_user_model().objects.create(email='admin@example.com', is_staff=True, is_superuser=True)
        self.client.force_login(self.superuser)
        self.group = Group.objects.create(name='Editors')
        self.permission = Permission.objects.get(codename='add_articlesmodel')
        self.group.permissions.add(self.permission)

    def test_create_article_as_non_superuser(self):
        non_superuser = get_user_model().objects.create(email='editor@example.com')
        non_superuser.groups.add(self.group)
        self.client.force_login(non_superuser)
        data = {
            'title': 'Test Article',
            'content': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.',
            'article_type': 'News',
        }
        response = self.client.post(reverse('add article view'), data)
        self.assertEqual(response.status_code, 302)


