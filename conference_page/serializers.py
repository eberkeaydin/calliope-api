# Django Rest Framework
from rest_framework import serializers

# Calliope | ConferencePage
from .models import (
    ConferencePage,
    SurveyQuestion,
    SurveyAnswer
)


class ConferencePageSerializer(serializers.ModelSerializer):

    class Meta: 
        model = ConferencePage
        fields = [
            'id',
            'code_editor_url',
            'directive_header',
            'directive_text',
            'is_active'
        ]


class SurveyAnswerSerializer(serializers.ModelSerializer):


    class Meta:

        model = SurveyAnswer
        fields = [
            'id',
            'related_survey',
            'survey_answer'
        ]

class SurveyQuestionSerializer(serializers.ModelSerializer):


    class Meta:

        model = SurveyQuestion
        fields = [
            'id',
            'survey_question',
            'is_active'
        ]
