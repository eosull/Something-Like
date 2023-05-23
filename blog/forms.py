from .models import Comment, Post, Category
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit


class PostForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'new-post-form'
        self.helper.form_class = 'content-form'
        self.helper.form_method = 'post'
        self.helper.form_action = 'submit_post'

        self.helper.add_input(Submit('submit', 'Submit'))

    class Meta:
        model = Post
        fields = ('title', 'category', 'body_text',)
        labels = {
            "title": ("Title"),
            "category": ("Type"),
            "body_text": ("What do you like about it?")
        }
        help_texts = {
            "title": ("Include Name of Work and Creator")
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body_text',)