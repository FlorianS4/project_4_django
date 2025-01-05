from django.contrib import admin
from .models import Post, Comment
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):

    list_display = ('post_name', 'status')
    search_fields = ['post_name',]
    list_filter = ('status', 'created_on',)
    summernote_fields = ('post_field',)

# Register your models here.
admin.site.register(Comment)
