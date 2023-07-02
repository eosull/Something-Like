from .models import Comment, Post, Category
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Submit
from allauth.account.forms import SignupForm, LoginForm


# Inheriting from Django ModelForm to create a new post form
class PostForm(forms.ModelForm):

    # Meta class outlining what model, fields and help texts to use
    class Meta:
        model = Post
        fields = ('title', 'category', 'body_text',)
        help_texts = {
            'category': ('Category'),
        }

    # Using __init__ to customise form
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Using CrispyForms FormHelper to add submit button
        self.helper = FormHelper(self)
        self.helper.add_input(Submit('submit', 'Submit'))

        # Adding placeholder texts for fields
        placeholders = {
            'title': 'Name and Creator of book, album, film, song....',
            'category': '',
            'body_text': """Tell everyone what you like - 
            style, length, actors etc. The more info you give
            the better recommendations you\'ll get!"""
        }

        # Autofocus 'title' field when page loaded
        self.fields['title'].widget.attrs['autofocus'] = True

        # Cycle through fields included in form to include
        # Placeholder text, add class for styling, remove labels
        # & increase the size of text area input box
        for field in self.fields:
            placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'new-post-form-inputs'
            self.fields[field].label = False
            self.fields[field].widget.attrs['rows'] = 6


# Inheriting from Django ModelForm to create a new comment form
class CommentForm(forms.ModelForm):

    # Meta class outlining what model and fields to use
    class Meta:
        model = Comment
        fields = ('body_text',)

    # Using __init__ to customise form
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Adding placeholder texts for input field
        placeholders = {
            'body_text': 'Add a recommendation or join the conversation....'
        }

        # Cycle through fields included in form to include
        # Placeholder text, add class for styling, remove labels
        # & increase the size of text area input box
        for field in self.fields:
            placeholder = placeholders[field]
            self.fields[field].widget.attrs['rows'] = 1
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'comment-form-input'
            self.fields[field].label = False


# Inheriting from Django Form to create filter form for explore page  
class PostCategoryFilterForm(forms.Form):

    # Declaring category options to be used
    CATEGORIES = (
        ("All", "All"),
        ("Music", "Music"),
        ("Tv", "Tv"),
        ("Films", "Films"),
        ("Books", "Books"),
    )

    # Declaring Date options to be used
    DATE_ORDER = (
        ("newest", "Newest First"),
        ("oldest", "Oldest First"),
    )

    # Creating the input fields using radio select widget
    # and pulling from category options above
    category = forms.ChoiceField(
        widget=forms.RadioSelect,
        choices=CATEGORIES,
        required=False
    )

    # Creating the input fields using radio select widget
    # and pulling from date options above
    date_order = forms.ChoiceField(
        label='Order By',
        widget=forms.RadioSelect,
        choices=DATE_ORDER,
        initial=False,
        required=False
    )


# Creating custom Signup form inheriting from Allauth Forms
class CustomRegisterForm(SignupForm):

    # Adding css class to input fields to style
    def __init__(self, *args, **kwargs):
        super(CustomRegisterForm, self).__init__(*args, **kwargs)
        for fieldname, field in self.fields.items():
            field.widget.attrs.update({
                'class': 'account-form-input',
            })


# Creating custom Login form inheriting from Allauth Forms
class CustomLoginForm(LoginForm):

    # Adding css class to input fields to style
    def __init__(self, *args, **kwargs):
        super(CustomLoginForm, self).__init__(*args, **kwargs)
        for fieldname, field in self.fields.items():
            field.widget.attrs.update({
                'class': 'account-form-input'
            })
