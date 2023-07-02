from django.db import models
from django.contrib.auth.models import User


# Category Model
class Category(models.Model):

    # Single type value, using char field
    type = models.CharField(max_length=200, unique=True)

    # __str__ to return type
    def __str__(self):
        return self.type


# Post Model
class Post(models.Model):

    # Slug Generated from Title created by user
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True, null=True)
    # Author assigned to post by pulling from User model,
    # on delete = CASCADE to delete user content if account deleted
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name='blog_posts')
    # Category defined by selecting one of the 'type' category model options
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    # created_at assigned on creation of post
    # edited_at updated each time post is edited
    created_at = models.DateTimeField(auto_now_add=True)
    edited_at = models.DateTimeField(auto_now=True)
    # Text field for post content input
    body_text = models.TextField()
    # Likes field so users can add a like to a post
    likes = models.ManyToManyField(User, related_name="post_like", blank=True)

    # Ordered by category
    class Meta:
        ordering = ['category']

    # String returns post title
    def __str__(self):
        return self.title

    # Counts and returns amount of likes on a post
    def number_of_likes(self):
        return self.likes.count()

    # Compares created_at & edited_at values to
    # see if post has been edited after creation.
    # .replace(microsecond=0) is used to set
    # Microsecond value to 0 for both.
    # See readme bugs section for more info on why
    def edited(self):
        if self.created_at.replace(
           microsecond=0) == self.edited_at.replace(microsecond=0):
            return False
        else:
            return True


# Comment Model
class Comment(models.Model):

    # Author assigned to post by pulling from User model,
    # on delete = CASCADE to delete user content if account deleted
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name='comments')
    # Post assigned to post by pulling from Post model,
    # on delete = CASCADE to delete post content if post deleted
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                             related_name='comments')
    # Created at time assigned on creation
    created_at = models.DateTimeField(auto_now_add=True)
    # Comment body text in text field
    body_text = models.TextField()
    # Comment approved boolean
    approved = models.BooleanField(default=False)
    # Likes field so user can leave a like on a comment
    likes = models.ManyToManyField(User, related_name="comment_like",
                                   blank=True)

    # Ordered by creation time, oldest first
    class Meta:
        ordering = ['created_at']

    # String returns comment and author
    def __str__(self):
        return f"{self.body_text} by {self.author}"

    # Counts and returns number of likes
    def number_of_likes(self):
        return self.likes.count()
