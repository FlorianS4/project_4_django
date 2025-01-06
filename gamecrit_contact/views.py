from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import GameCritContact

# Create your views here.

class GameCritContactList(generic.ListView):
    queryset = GameCritContact.objects.all().order_by("created_on")
    template_name = "gamecrit_contact/gamecrit_contact.html"
    paginate_by = 3

