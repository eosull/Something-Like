from django.test import TestCase
from blog.models import Category, Post, Comment, User
import datetime


class CategoryTestCase(TestCase):
    def setUp(self):
        # Creating test category instance
        Category.objects.create(type="Music")

    def test_type_return(self):
        # Category __str__ return category type
        category = Category.objects.get(type="Music")
        self.assertEqual(category.__str__(), "Music")


class PostTestCase(TestCase):
    def setUp(self):
        # Creating test post instance, including test user and category
        self.user = User.objects.create_user(username='testuser', password='password')
        self.category = Category.objects.create(type="Test")
        Post.objects.create(title="Test Case", author=self.user,
                            category=self.category, body_text="Test body content")

    def test_title_return(self):
        # Post __str__ function return post title
        post = Post.objects.get(title="Test Case")
        self.assertEqual(post.__str__(), "Test Case")

    def test_post_like_number(self):
        # Post number_of_likes returns like number (0 on creation)
        post = Post.objects.get(title="Test Case")
        self.assertEqual(post.number_of_likes(), 0)

    def test_post_edited_status(self):
        # Post edited function returns True if edited time different to created time
        post = Post.objects.get(title="Test Case")
        self.assertEqual(post.edited(), False)
        # Adding 1 day to edited time to simulate editing
        post.edited_at += datetime.timedelta(days=1)
        self.assertEqual(post.edited(), True)


class CommentTestCase(TestCase):
    def setUp(self):
        # Creating test comment instance including test user and post including test poster and category
        self.user = User.objects.create_user(username='testuser', password='password')
        post_user = User.objects.create_user(username='poster', password='password')
        post_category = Category.objects.create(type="Test")
        self.post = Post.objects.create(title="Test Post", author=post_user, category=post_category)
        Comment.objects.create(author=self.user, post=self.post, body_text="Test Comment")

    def test_comment_return(self):
        # Comment __str__ returns comment and user
        comment = Comment.objects.get(body_text="Test Comment")
        self.assertEqual(comment.__str__(), "Test Comment by testuser")

    def test_comment_like_number(self):
        # Comment number_of_likes function returns like number (0 on creation)
        comment = Comment.objects.get(body_text="Test Comment")
        self.assertEqual(comment.number_of_likes(), 0)