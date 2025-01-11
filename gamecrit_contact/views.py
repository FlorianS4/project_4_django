from django.shortcuts import render
from django.contrib import messages
from .models import GameCritContact
from .forms import GameCritContactForm

# Create your views here.

def gamecrit_contact(request):
    """
    User can get in contact with site owner
    """

    if request.method == "POST":
        contact_form = GameCritContactForm(data=request.POST)
        if contact_form.is_valid():
            contact_form.save()
            messages.add_message(request, messages.SUCCESS, "Hey, thanks for your message. I will check it out and contact you in the next 3 days.")
    contact_form = GameCritContactForm()

    return render(
        request,
        "gamecrit_contact.html",
        {
           "contact_form": contact_form,  
        }
    )
