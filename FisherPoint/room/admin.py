from django.contrib import admin

from FisherPoint.room.models import Room


@admin.register(Room)
class UserAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'created_at', 'updated_at']
    list_filter = ['name']
    search_fields = ['name']
    ordering = ['created_at']