from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Post


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
            },
        )
