from .models import Post, Comment
from django import forms


class GamecritPostForm(forms.ModelForm):
    """
    Gamecrit Post Form, creating a form for the user so he can create a post himself
    """
    class Meta:
        model = Post
        fields = ('post_name', 'post_field', 'post_image', 'youtube_link',)


class GameCritCommentForm(forms.ModelForm):
    """
    Gamecrit Comment Form, creating a form for the user so he can ceate a comment himself
    """
    class Meta:
        model = Comment
        fields = ('comment_field',)