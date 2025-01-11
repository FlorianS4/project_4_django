from django.shortcuts import render
from .models import GameCritContact
from .forms import GameCritContactForm

# Create your views here.

def gamecrit_contact(request):
    """
    User can get in contact with site owner
    """
    contact_form = GameCritContactForm()

    return render(
        request,
        "gamecrit_contact.html",
        {
           "contact_form": contact_form,  
        }
    )
