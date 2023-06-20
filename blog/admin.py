from django.contrib import admin
from .models import Post, Category, Comment
from django_summernote.admin import SummernoteModelAdmin


# Register Post Model Admin Panel
@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):

    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('category', 'created_at')
    list_display = ('title', 'category', 'author', 'created_at')
    summernote_fields = 'body_text'


# Register Comment Model Admin Panel
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):

    list_display = ('post', 'author', 'created_at', 'body_text', 'approved')
    list_filter = ('approved', 'created_at')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)


# Register Category Model Admin Panel
admin.site.register(Category)
