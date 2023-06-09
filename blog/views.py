from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.http import HttpResponseRedirect
from django.views import generic, View
from django.contrib import messages
import string

from .models import Post, Category, Comment
from .forms import CommentForm, PostForm, PostCategoryFilterForm


# Inherit from Django ListView for landing page
class IndexList(generic.ListView):
    # Take 3 most recent posts from Post Model for display
    queryset = Post.objects.order_by('created_at').reverse()[:3]
    template_name = "index.html"


# Function for Explore page
def explore(request):
    # Check if category & date_order specified from filter form
    category = request.GET.get('category')
    date_order = request.GET.get('date_order')
    # Get all posts
    posts = Post.objects.all()
    # If category or date specified, order posts in that way
    if category:
        if category != 'All':
            posts = posts.filter(category__type=category)
    if date_order == 'oldest':
        posts = posts.order_by('created_at')
    else:
        posts = posts.order_by('-created_at')
    # Define context to be sent to template
    context = {
        'form': PostCategoryFilterForm(),
        'post_list': posts,
        'category_list': Category.objects.all()
    }
    # Render the page
    return render(request, 'explore.html', context)


# Inherit from Django view for NewPost Class
class NewPost(View):

    # Getting template and form to display page
    def get(self, request, *arg, **kwargs):

        return render(
            request,
            'new_post.html',
            {
                "new_post_form": PostForm(),
            }
        )

    # Posting new post form
    def post(self, request, *arg, **kwargs):

        # Defining form imported from .forms
        new_post_form = PostForm(data=request.POST)

        # Checking if form is valid
        if new_post_form.is_valid():
            # email,name,author_id pulled from User
            new_post_form.instance.email = request.user.email
            new_post_form.instance.name = request.user.username
            new_post_form.instance.author_id = request.user.id
            # slug generated from title, removing string characters from title
            new_post_form.instance.slug = new_post_form.instance.title.translate(
                str.maketrans(
                        '', '', string.punctuation)).lower().replace(" ", "-")
            # saving new post
            new_post = new_post_form.save(commit=False)
            new_post.save()
            # Notify user of successful post creation
            messages.success(
                request, f'Post: {new_post_form.instance.title} created')
            # Redirect user to the new post page
            return redirect('post_detail', slug=new_post.slug)
        # If form not valid empty form
        else:
            new_post_form = PostForm()

        # Return form
        return render(
            request,
            'new_post.html',
            {
                "new_post_form": PostForm(),
            },
        )

    # Editing post, taking slug to specify post
    def edit(request, slug):
        # Finding post based on slug
        post = get_object_or_404(Post, slug=slug)
        # If method is POST get form filled with post details
        if request.method == 'POST':
            edit_post_form = PostForm(request.POST, instance=post)
            # If form is valid save and notify user of success,
            # redirecting to post detail page
            if edit_post_form.is_valid():
                edit_post_form.save()
                messages.success(request, f'{post.title} edited successfully')
                return redirect('post_detail', slug=post.slug)
        # Return edit post form and post to be rendered
        edit_post_form = PostForm(instance=post)
        context = {
            'edit_post_form': edit_post_form,
            'post': post,
        }
        return render(request, "edit_post.html", context)

    # Delete post, taking slug to specify post
    def delete(request, slug):
        # Finding post based on slug
        post = get_object_or_404(Post, slug=slug)

        # If method is POST, delete post and return delete message
        if request.method == 'POST':
            post.delete()
            messages.error(request, f'Post: {post.title} deleted succesfully')
            # Redirect to home after delete
            return redirect('home')
        # Return delete confirmation page
        else:
            return render(
                request,
                'delete_post.html',
                {
                    'post': post
                }
            )


# Inherit Django View class for Post Detail view
class PostDetail(View):

    # Get function for displaying content
    def get(self, request, slug, *arg, **kwargs):

        # Get post based on slug, comments taken from this post
        queryset = Post.objects
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by('created_at')

        # Checking if user has liked post
        post_liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            post_liked = True

        # Return context for use in template declared
        return render(
            request,
            "post_detail.html",
            {
                "all_posts": queryset,
                "post": post,
                "comments": comments,
                "commented": False,
                "comment_form": CommentForm(),
                "post_liked": post_liked,
            },
        )

    # Post function for adding comments
    def post(self, request, slug, *arg, **kwargs):

        # Get post based on slug, comments taken from this post
        queryset = Post.objects
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by('created_at')

        # Defining comment form using imported form
        comment_form = CommentForm(data=request.POST)

        # If form valid fill info with user's details and save
        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment_form.instance.author_id = request.user.id
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
        # Else post empty form
        else:
            comment_form = CommentForm()

        # Return context for use in template declared
        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": True,
                "comment_form": comment_form,
            },
        )


# Inherit Django View class to create Post Liking view
class PostLike(View):

    def post(self, request, slug):
        # Getting post based on slug
        post = get_object_or_404(Post, slug=slug)

        # If user has liked post, clicking button unlikes
        # and vice-versa
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        # Reload post detail page
        return HttpResponseRedirect(reverse('post_detail', args=[slug]))


# Inherit Django View class to create Comment Liking view
class CommentLike(View):

    def post(self, request, slug, id):
        # Getting comment based on id
        comment = get_object_or_404(Comment, id=id)

        # If user has liked comment, clicking button unlikes
        # and vice-versa
        if comment.likes.filter(id=request.user.id).exists():
            comment.likes.remove(request.user)
        else:
            comment.likes.add(request.user)

        # Reload post detail page
        return HttpResponseRedirect(reverse('post_detail', args=[slug]))
