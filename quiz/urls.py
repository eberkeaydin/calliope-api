# Django
from django.urls import path

# Calliope | Quiz
from .views import Quiz, QuizQuestion

app_name = 'quiz'

urlpatterns = [
    path('', Quiz.as_view(), name='quiz'),
    path('q/<str:quiz_id>/', QuizQuestion.as_view(), name='questions'),
]
