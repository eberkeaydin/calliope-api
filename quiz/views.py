from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Quizzes, Question
from .serializers import QuizSerializer, QuestionSerializer

class Quiz(generics.ListAPIView):
    
    serializer_class = QuizSerializer
    queryset = Quizzes.objects.all()

class QuizQuestion(APIView):
    def get(self, request, **kwargs):
        question = Question.objects.filter(quiz__title=kwargs['topic'])
        serializer = QuestionSerializer(question, many=True)
        return Response(serializer.data)