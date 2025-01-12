from .models import Post, Comment
from django import forms


class GamecritPostForm(forms.ModelForm):
    """
    Form to create a post
    """
    class Meta:
        model = post
        fields = ('post_name', 'slug', 'post_field', 'youtube_link',)


class GameCritCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment_field',)