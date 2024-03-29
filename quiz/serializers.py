# Django Rest Framework
from rest_framework import serializers

# Calliope | Quiz
from .models import Answer, Question, Quizzes


class QuizSerializer(serializers.ModelSerializer):

    class Meta: 
        model = Quizzes
        fields = [
            'id',
            'category',
            'title',
            'related_lesson',
            'date_created'
        ]


class AnswerSerializer(serializers.ModelSerializer):

    class Meta:

        model = Answer
        fields = [
            'id',
            'answer_text',
            'is_right',
        ]


class QuestionSerializer(serializers.ModelSerializer):

    answer = AnswerSerializer(many=True, read_only=True)
    quiz = QuizSerializer(read_only=True)

    class Meta:

        model = Question
        fields = [
            'id',
            'quiz',
            'title',
            'question_text',
            'answer',
            'date_created',
            'difficulty',
            'is_active'
        ]
