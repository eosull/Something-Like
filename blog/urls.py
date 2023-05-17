from . import views
from django.urls import path

urlpatterns = [
    path('', views.IndexList.as_view(), name='home'),
    path('explore', views.ExploreList.as_view(), name='explore'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('new_post', views.NewPost.as_view(), name='new_post'),
    path('edit/<slug>', views.NewPost.edit, name='edit'),
    path('delete/<slug>', views.NewPost.delete, name='delete'),
]
