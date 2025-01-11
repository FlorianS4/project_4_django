from .models import GameCritContact
from django import forms

class GameCritContactForm(forms.ModelForm):
    class Meta: 
        model = GameCritContact
        fields = ('contact_name', 'contact_email', 'contact_field')