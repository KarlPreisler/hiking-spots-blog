from django.test import TestCase, Client
from django.urls import reverse
from .models import Post
from django.contrib.auth import get_user_model

User = get_user_model()


class TestViews(TestCase):

    @classmethod
    def setUpTestData(self):
        """ Create test data """
        self.user = User.objects.create(username='testdummy')
        self.user.set_password('543210')
        self.user.save()

        self.post = Post.objects.create(
            title='Testdummy Post',
            slug='testdummy-post',
            author=self.user,
            content='content from testdummy',
            excerpt='testdummy excerpt',
            difficulty='E',
            featured_image='placeholder',
            status=1
        )

    def test_get_post_list_view(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')
        self.assertTemplateUsed(response, 'base.html')
