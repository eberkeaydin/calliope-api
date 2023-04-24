# Django Rest Framework
from rest_framework import serializers

# Calliope | Quiz
from .models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta: 
        model = User
        fields = [
            'id',
            'user_name',
            'role',
            'score'
        ]
