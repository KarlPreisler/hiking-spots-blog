from django.test import TestCase
from .forms import CommentForm, AddPostForm, EditPostForm


class TestCommentForm(TestCase):
    """
    Unit testing for add comment form
    """
    def test_message_field_is_required(self):
        form = CommentForm({'body': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('body', form.errors.keys())
        self.assertEqual(form.errors['body'][0], 'This field is required.')

    def test_fields_are_explicit_in_form_metaclass(self):
        form = CommentForm()
        self.assertEqual(form.Meta.fields, ('body',))


class TestAddPostForm(TestCase):
    """
    Unit testing for add post form
    """
    def test_title_is_required(self):
        form = AddPostForm({'title': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('title', form.errors.keys())
        self.assertEqual(form.errors['title'][0], 'This field is required.')

    def test_slug_is_required(self):
        form = AddPostForm({'slug': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('slug', form.errors.keys())
        self.assertEqual(form.errors['slug'][0], 'This field is required.')

    def test_content_is_required(self):
        form = AddPostForm({'content': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('content', form.errors.keys())
        self.assertEqual(form.errors['content'][0], 'This field is required.')

    def test_difficulty_is_required(self):
        form = AddPostForm({'difficulty': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('difficulty', form.errors.keys())
        self.assertEqual(
            form.errors['difficulty'][0], 'This field is required.')

    def test_fields_are_explicit_in_form_metaclass(self):
        form = AddPostForm()
        self.assertEqual(form.Meta.fields, ('__all__'))


class TestEditPostForm(TestCase):
    """
    Unit testing for edit post form
    """
    def test_title_is_required(self):
        form = EditPostForm({'title': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('title', form.errors.keys())
        self.assertEqual(form.errors['title'][0], 'This field is required.')

    def test_slug_is_required(self):
        form = EditPostForm({'slug': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('slug', form.errors.keys())
        self.assertEqual(form.errors['slug'][0], 'This field is required.')

    def test_content_is_required(self):
        form = EditPostForm({'content': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('content', form.errors.keys())
        self.assertEqual(form.errors['content'][0], 'This field is required.')

    def test_difficulty_is_required(self):
        form = EditPostForm({'difficulty': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('difficulty', form.errors.keys())
        self.assertEqual(
            form.errors['difficulty'][0], 'This field is required.')

    def test_fields_are_explicit_in_form_metaclass(self):
        form = EditPostForm()
        self.assertEqual(form.Meta.fields, ('__all__'))
