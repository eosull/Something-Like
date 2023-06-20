from django.test import TestCase, Client
from django.urls import reverse
from .models import Post, Category, Comment, User


class IndexViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('home')

    def test_index_view(self):
        # Testing Succesful get request and correct template file in use
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')


class ExploreViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('explore')

    def test_explore_view(self):
        # Testing Succesful get request and correct template file in use
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'explore.html')


class NewPostViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('new_post')

    def test_new_post_view(self):
        # Testing Succesful get request and correct template file in use
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'new_post.html')


class EditPostViewTestCase(TestCase):
    def setUp(self):
        # Creating test case category, user and post
        category = Category.objects.create(type="Test")
        user = User.objects.create_user(username='testuser',
                                        password='password')
        self.post = Post.objects.create(title="Test Post", author=user,
                                        category=category, slug='test-post')
        self.client = Client()
        self.url = reverse('edit', args=['test-post'])

    def test_edit_post_view(self):
        # Testing Succesful get request and correct template file in use
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'edit_post.html')


class DeletePostViewTestCase(TestCase):
    def setUp(self):
        # Creating test case category, user and post
        category = Category.objects.create(type="Test")
        user = User.objects.create_user(username='testuser',
                                        password='password')
        self.post = Post.objects.create(title="Test Post", author=user,
                                        category=category, slug='test-post')
        self.client = Client()
        self.url = reverse('delete', args=['test-post'])

    def test_edit_post_view(self):
        # Testing Succesful get request and correct template file in use
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'delete_post.html')


class PostDetailViewTestCase(TestCase):
    def setUp(self):
        # Creating test case category, user and post
        category = Category.objects.create(type="Test")
        user = User.objects.create_user(username='testuser',
                                        password='password')
        self.post = Post.objects.create(title="Test Post", author=user,
                                        category=category, slug='test-post')
        self.client = Client()
        self.url = reverse('post_detail', args=['test-post'])

    def test_edit_post_view(self):
        # Testing Succesful get request and correct template file in use
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'post_detail.html')


class PostLikeViewTestCase(TestCase):
    def setUp(self):
        # Creating test case category, user and post
        self.category = Category.objects.create(type="Test")
        self.user = User.objects.create_user(username='testuser',
                                             password='password')
        self.post = Post.objects.create(title="Test Post", author=self.user,
                                        category=self.category,
                                        slug='test-post')
        self.client = Client()
        self.url = reverse('post_like', args=['test-post'])

    def test_edit_post_view(self):
        # Testing Succesful post and redirect using 302 status code
        self.client.force_login(self.user)
        response = self.client.post(self.url)
        self.assertEqual(response.status_code, 302)


class CommentLikeViewTestCase(TestCase):
    def setUp(self):
        # Creating test case category, user and post
        self.category = Category.objects.create(type="Test")
        self.user = User.objects.create_user(username='testuser',
                                             password='password')
        self.post = Post.objects.create(title="Test Post", author=self.user,
                                        category=self.category,
                                        slug='test-post')
        self.comment = Comment.objects.create(author=self.user, post=self.post,
                                              body_text="Test Comment")
        self.client = Client()
        self.url = reverse('comment_like', args=['test-post', self.comment.id])

    def test_edit_post_view(self):
        # Testing Succesful post and redirect using 302 status code
        self.client.force_login(self.user)
        response = self.client.post(self.url)
        self.assertEqual(response.status_code, 302)