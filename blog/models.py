from django.db import models
import uuid
from accounts.models import CustomUser


class Category(models.Model):
    id = models.IntegerField(primary_key=True)
    type = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.type


class Post(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='blog_posts')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=200, unique=True)
    body_text = models.TextField()
    edited = False

    class Meta:
        ordering = ['category']

    def __str__(self):
        return self.title


class Comment(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='comments')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    created_at = models.DateTimeField(auto_now_add=True)
    body_text = models.TextField()
    edited = False

    class Meta:
        ordering = ['created_at']

    def __str__(self):
        return f"Comment by {self.author} on {self.created_at}"
