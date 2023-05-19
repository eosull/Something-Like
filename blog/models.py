from django.db import models
from django.contrib.auth.models import User
import uuid


class Category(models.Model):

    type = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.type


class Post(models.Model):

    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    body_text = models.TextField()
    likes = models.ManyToManyField(User, related_name="post_like", blank=True)
    edited = False

    class Meta:
        ordering = ['category']

    def __str__(self):
        return self.title
    
    def number_of_likes(self):
        return self.likes.count()


class Comment(models.Model):

    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    created_at = models.DateTimeField(auto_now_add=True)
    body_text = models.TextField()
    approved = models.BooleanField(default=False)
    edited = False

    class Meta:
        ordering = ['created_at']

    def __str__(self):
        return f"Comment by {self.author} on {self.created_at}"
