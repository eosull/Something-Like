from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.http import HttpResponseRedirect
from django.views import generic, View
from django.contrib import messages

from .models import Post, Category, Comment
from .forms import CommentForm, PostForm, PostCategoryFilterForm


class IndexList(generic.ListView):
    queryset = Post.objects.all()
    template_name = "index.html"
    ordering = ['-created_at']
    paginate_by = 3


def explore(request):
    category = request.GET.get('category')
    date_order = request.GET.get('date_order')
    posts = Post.objects.all()
    if category:
        if category != 'All':
            posts = posts.filter(category__type=category)
    if date_order:
        posts = posts.order_by('-created_at')
    
    context = {
        'form': PostCategoryFilterForm(),
        'post_list': posts,
        'category_list': Category.objects.all()
    }
    return render(request, 'explore.html', context)


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
            messages.success(request, f'Post: {new_post_form.instance.title} created successfully')
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
                messages.success(request, f'{post.title} edited successfully')
                return redirect('post_detail', slug=post.slug)
        edit_post_form = PostForm(instance=post)
        context = {
            'edit_post_form': edit_post_form,
            'post': post,
        }
        return render(request, "edit_post.html", context)

    def delete(request, slug):
        post = get_object_or_404(Post, slug=slug)

        if request.method == 'POST':
            post.delete()
            messages.error(request, f'Post: {post.title} deleted succesfully')
            return redirect('home')

        else:
            return render(
                request,
                'delete_post.html',
                {
                    'post': post
                }
            )


class PostDetail(View):

    def get(self, request, slug, *arg, **kwargs):

        queryset = Post.objects
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by('created_at')

        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True
        
        return render(
            request,
            "post_detail.html",
            {
                "all_posts": queryset,
                "post": post,
                "comments": comments,
                "commented": False,
                "comment_form": CommentForm(),
                "liked": liked,
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


class PostLike(View):

    def post(self, request, slug):
        post = get_object_or_404(Post, slug=slug)

        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('post_detail', args=[slug]))


class CommentLike(View):

    def post(self, request, slug, id):
        comment = get_object_or_404(Comment, id=id)

        if comment.likes.filter(id=request.user.id).exists():
            comment.likes.remove(request.user)
        else:
            comment.likes.add(request.user)

        return HttpResponseRedirect(reverse('post_detail', args=[slug]))
