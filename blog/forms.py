from .models import Comment, Post
from django import forms


class CommentForm(forms.ModelForm):
    """
    Form that allows users to comment on a post
    """
    class Meta:
        model = Comment
        fields = ('body',)


class AddPostForm(forms.ModelForm):
    """
    Form that allows admin to add a post
    """
    class Meta:
        model = Post
        fields = '__all__'


class EditPostForm(forms.ModelForm):
    """
    Form that allows admin to edit a post
    """
    class Meta:
        model = Post
        fields = '__all__'
