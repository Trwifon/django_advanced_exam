from django.contrib import admin
from django.template.defaultfilters import title

from FisherPoint.competition.models import Competition


@admin.register(Competition)
class UserAdmin(admin.ModelAdmin):
    list_display = ['title', 'location', 'date_of_event']
    list_filter = ['date_of_event']
    search_fields = ['title', 'location']
    ordering = ['date_of_event']