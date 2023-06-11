# Django
from rest_framework import serializers

# Calliope | Lesson
from .models import Category, Conference, Content, Lesson


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = [
            'id',
            'category_name'
        ]


class LessonSerializer(serializers.ModelSerializer):

    class Meta:

        model = Lesson
        category = CategorySerializer(many=True, read_only=True)

        fields = [
            'id',
            'lesson_title',
            'category',
            'difficulty',
            'date_created',
            'is_active'
        ]


class ContentSerializer(serializers.ModelSerializer):

    class Meta:

        model = Content
        related_lesson = LessonSerializer(many=True, read_only=True)

        fields = [
            'id',
            'related_lesson',
            'video_url',
            'content_header',
            'content_text'
        ]


class ConferenceSerializer(serializers.ModelSerializer):

    class Meta:

        model = Conference
        related_lesson = LessonSerializer(many=True, read_only=True)

        fields = [
            'id',
            'conference_topic',
            'conference_url',
            'related_lesson',
        ]
