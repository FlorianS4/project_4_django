from django.shortcuts import render
from .models import GameCritContact

# Create your views here.

def game_crit_contact(request):
    """
    User can get in contact with site owner
    """
    contact_form = ContactForm()

    return render(
        request,
        "gamecrit_contact/gamecrit_contact.html",
        {
           "contact_form": contact_form,  
        }
    )
