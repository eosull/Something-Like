from django.contrib import admin
from .models import Post, Category, Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Post, Comment, Category)
class PostAdmin(SummernoteModelAdmin):

    summernote_fields = 'body_text'
