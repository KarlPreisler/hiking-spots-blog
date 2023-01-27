from django.test import TestCase
from django.urls import reverse


class TestViews(TestCase):
    def test_get_post_list_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')