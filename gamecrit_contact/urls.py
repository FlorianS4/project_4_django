from . import views
from django.urls import path

urlpatterns = [
    path('', views.gamecrit_contact, name = 'gamecrit_contact')
]