from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Post, Comment

User = get_user_model()


class TestViews(TestCase):
    """
    Unit testing for post model
    """
    @classmethod
    def setUpTestData(self):
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

        self.comment = Comment.objects.create(
            post=self.post,
            body='test comment by testdummy'
        )

    def test_post_approved(self):
        self.assertFalse(self.post.status == 0)

    def test_comment_approved(self):
        self.assertFalse(self.comment.approved)
