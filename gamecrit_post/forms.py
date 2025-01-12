from .models import Post, Comment
from django import forms


class GamecritPostForm(forms.ModelForm):
    """
    Form to create a post
    """
    class Meta:
        model = Post
        fields = ('post_name', 'post_field', 'youtube_link',)


class GameCritCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment_field',)