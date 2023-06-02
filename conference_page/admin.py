# Django
from django.contrib import admin

# Calliope | ConferencePage
from . import models


@admin.register(models.ConferencePage)
class ConferencePageAdmin(admin.ModelAdmin):

    list_display = [
        'related_conference',
        'code_editor_url',
        'directive_text',
        'is_active'
    ]
