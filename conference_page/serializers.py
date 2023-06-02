# Django Rest Framework
from rest_framework import serializers

# Calliope | ConferencePage
from .models import ConferencePage


class ConferencePageSerializer(serializers.ModelSerializer):

    class Meta: 
        model = ConferencePage
        fields = [
            'id',
            'related_conference',
            'code_editor_url',
            'directive_text',
            'is_active'
        ]
