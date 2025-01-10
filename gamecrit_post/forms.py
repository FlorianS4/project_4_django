from .models import Comment
from django import forms


class GameCritCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment_field',)