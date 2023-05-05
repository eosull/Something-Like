from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('explore', views.ExplorePosts.as_view(), name='explore'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('new_post', views.NewPost.as_view(), name='new_post'),
]
