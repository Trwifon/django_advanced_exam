from django.contrib import admin
from . models import Message


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ['body']
    search_fields = ['body']



