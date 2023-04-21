# Django
from django.urls import path

# Calliope | Lesson 
from .views import CategoryView, LessonView, ContentView, ConferenceView

app_name = 'lesson'  

urlpatterns = [  
    path('category/', CategoryView.as_view(), name='category'),
    path('lesson/', LessonView.as_view(), name='lesson'),
    path('content/', ContentView.as_view(), name='content'),
    path('conference/', ConferenceView.as_view(), name='conference')
]  