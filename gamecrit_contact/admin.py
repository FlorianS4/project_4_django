from django.contrib import admin
from .models import GameCritContact
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.


@admin.register(GameCritContact)
class ContactAdmin(SummernoteModelAdmin):

    list_display = ('contact_email', 'contact_field',)
    search_fields = ['contact_email', ]
    list_filter = ('contact_email',)
    summernote_fields = ('contact_field',)
