# Django Rest Framework
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

# Calliope | Quiz
from .models import Question, Quizzes
from .serializers import QuestionSerializer, QuizSerializer


class Quiz(generics.ListAPIView):

    serializer_class = QuizSerializer
    queryset = Quizzes.objects.all()


class QuizQuestion(APIView):

    def get(self, request, **kwargs):
        question = Question.objects.filter(quiz__id=kwargs['quiz_id'])
        serializer = QuestionSerializer(question, many=True)
        return Response(serializer.data)
