# Django
from django.contrib import admin

# Calliope | User
from . import models


@admin.register(models.User)
class UserAdmin(admin.ModelAdmin):

    list_display = [
        'user_name',
        'role'
    ]
