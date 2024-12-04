from django.contrib import admin

from FisherPoint.account.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'first_name', 'last_name', 'avatar', 'is_staff']
    list_filter = ['username']
    search_fields = ['username', 'email']
    ordering = ['username']