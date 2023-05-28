from .models import Comment, Post, Category
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Submit


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'category', 'body_text',)
        help_texts = {
            'category' : ('Category'),
        }


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.add_input(Submit('submit', 'Submit'))

        placeholders = {
            'title': 'Name and Creator of book, album, film, song....',
            'category': '',
            'body_text': 'Tell everyone what you like - style, length, actors etc. The more info you give the better recommendations you\'ll get!'
        }

        self.fields['title'].widget.attrs['autofocus'] = True

        for field in self.fields:

            placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'new-post-form-inputs'
            self.fields[field].label = False


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body_text',)
 
        
class PostCategoryFilterForm(forms.Form):

    CATEGORIES = (
        ("All", "All"),
        ("Music", "Music"),
        ("Tv", "Tv"),
        ("Films", "Films"),
        ("Books", "Books"),
        ("Test", "Test"),
    )

    DATE_ORDER = (
        ("newest", "Newest First"),
        ("", "Oldest First"),
    )

    category = forms.ChoiceField(
        widget=forms.RadioSelect,
        choices = CATEGORIES,
        required = False
    )
    
    date_order = forms.ChoiceField(
        label = 'Order By',
        widget = forms.RadioSelect,
        choices = DATE_ORDER,
        initial = False,
        required = False
    )