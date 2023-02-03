from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.urls import reverse

STATUS = ((0, "Draft"), (1, "Published"))

DIFFICULTY_CHOICES = (
    ('Easiest', 'E'),
    ('Moderate', 'M'),
    ('Moderately Strenous', 'MS'),
    ('Strenous', 'S'),
    ('Very Strenous', 'VS'),
)


class Post(models.Model):
    """
    Model for all posts
    """
    title = models.CharField(max_length=200, unique=True, default='Title')
    slug = models.SlugField(max_length=200, unique=True, default='slug')
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField(default='Content')
    featured_image = CloudinaryField(
        'image', default='placeholder')
    excerpt = models.TextField(blank=True, default='Excerpt')
    created_on = models.DateTimeField(auto_now_add=True)
    difficulty = models.CharField(
        'Difficulty', max_length=20, blank=False, choices=DIFFICULTY_CHOICES,
        default='Difficulty Level')
    latitude = models.FloatField('Latitude', blank=True, null=True)
    longitude = models.FloatField('Longitude', blank=True, null=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(User, related_name='blog_likes', blank=True)

    class Meta:
        """
        Sorts posts to show newest post first
        """
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()

    def get_absolute_url(self):
        return reverse('post_detail', args=(str(self.id)))


class Comment(models.Model):
    """
    Model for comment field underneath posts
    """
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        """
        Sorts comments to show newest comment first
        """
        ordering = ['-created_on']

    def __str__(self):
        return f"Comment {self.body} by {self.name}"
