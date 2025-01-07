from . import views
from django.urls import path

urlpatterns = [
    path('', views.GameCritContactList.as_view(), name = 'gamecrit_contact_url')
]