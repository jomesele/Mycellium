from django.contrib import admin
from .models import AlowedUsers

@admin.register(AlowedUsers)
class AlowedUsersAdmin(admin.ModelAdmin):
    '''AllowedUsers management config'''
    list_display = ['phone']