from . import views
from django.urls import path

# Importing URL patterns for blog site
urlpatterns = [
    # Landing page
    path('', views.IndexList.as_view(), name='home'),
    # Explore posts
    path('explore', views.explore, name='explore'),
    # Individual post detail
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    # New post form
    path('new_post', views.NewPost.as_view(), name='new_post'),
    # Edit post page
    path('edit/<slug>', views.NewPost.edit, name='edit'),
    # Delete post
    path('delete/<slug>', views.NewPost.delete, name='delete'),
    # Add like to post
    path('<slug:slug>', views.PostLike.as_view(), name='post_like'),
    # Add like to comment
    path('<slug:slug>/<int:id>', views.CommentLike.as_view(), name='comment_like'),
]
