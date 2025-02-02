from .models import GameCritContact
from django import forms


class GameCritContactForm(forms.ModelForm):
    """
    Gamecrit Contact Form
    """
    class Meta: 
        model = GameCritContact
        fields = ('contact_email', 'contact_field')
