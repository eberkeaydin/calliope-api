# Django
from django.contrib import admin

# Calliope | ConferencePage
from . import models


@admin.register(models.ConferencePage)
class ConferencePageAdmin(admin.ModelAdmin):

    list_display = [
        'code_editor_url',
        'directive_header',
        'directive_text',
        'is_active'
    ]


@admin.register(models.SurveyQuestion)
class SurveyAdmin(admin.ModelAdmin):

    list_display = [
        'survey_question',
    ]


@admin.register(models.SurveyAnswer)
class SurveyAnswerAdmin(admin.ModelAdmin):

    list_display = [
        'related_survey',
        'survey_answer'
    ]
