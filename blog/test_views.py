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
        self.user.set_password('test1234')
        self.user.is_superuser = True
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

    def test_get_post_detail_view(self):
        response = self.client.get(
            reverse('post_detail', args=[self.post.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'base.html')
        self.assertTemplateUsed(response, 'post_detail.html')

    # def test_get_add_post_view(self):
    #    self.client.login(username='testdummy', password='test1234')
    #    response = self.client.get(reverse('add_post'))
    #    self.assertEqual(response.status_code, 200)
    #    self.assertTemplateUsed(response, 'add_post.html')
    #    self.assertTemplateUsed(response, 'base.html')

    def test_get_about_view(self):
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'about.html')
        self.assertTemplateUsed(response, 'base.html')

    def test_get_difficulty_view(self):
        response = self.client.get(reverse('difficulty'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'difficulty.html')
        self.assertTemplateUsed(response, 'base.html')
