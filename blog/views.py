from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.views import generic, View

from .models import Post
from .forms import CommentForm, PostForm


class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.order_by('-created_at')
    template_name = 'index.html'
    paginate_by = 6


class ExplorePosts(generic.ListView):
    model = Post
    queryset = Post.objects.order_by('-created_at')
    template_name = 'explore.html'
    paginate_by = 6


class NewPost(View):

    def get(self, request, *arg, **kwargs):

        return render(
            request,
            'new_post.html',
            {
                "new_post_form": PostForm(),
            }
        )

    def post(self, request, *arg, **kwargs):

        new_post_form = PostForm(data=request.POST)

        if new_post_form.is_valid():
            new_post_form.instance.email = request.user.email
            new_post_form.instance.name = request.user.username
            new_post_form.instance.author_id = request.user.id
            new_post_form.instance.slug = new_post_form.instance.title.replace(' ', '-').lower()
            new_post = new_post_form.save(commit=False)
            new_post.save()
            return redirect('post_detail', slug=new_post.slug)
        else:
            new_post_form = PostForm()

        return render(
            request,
            'new_post.html',
            {
                "new_post_form": PostForm(),
            },
        )

    def edit(request, slug):
        post = get_object_or_404(Post, slug=slug)
        if request.method == 'POST':
            edit_post_form = PostForm(request.POST, instance=post)
            if edit_post_form.is_valid():
                edit_post_form.save()
                return redirect('post_detail', slug=post.slug)
        edit_post_form = PostForm(instance=post)
        context = {
            'edit_post_form': edit_post_form,
            'post': post,
        }
        return render(request, "edit_post.html", context)

    def delete(request, slug):
        post = get_object_or_404(Post, slug=slug)
        post.delete()
        return redirect('home')


class PostDetail(View):

    def get(self, request, slug, *arg, **kwargs):

        queryset = Post.objects
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by('created_at')

        return render(
            request,
            "post_detail.html",
            {
                "all_posts": queryset,
                "post": post,
                "comments": comments,
                "commented": False,
                "comment_form": CommentForm(),
            },
        )

    def post(self, request, slug, *arg, **kwargs):

        queryset = Post.objects
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by('created_at')

        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment_form.instance.author_id = request.user.id
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
        else:
            comment_form = CommentForm()

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

