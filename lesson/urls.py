# Django
from django.urls import path

# Calliope | Lesson 
from .views import (CategorySingularView, CategoryView, ConferenceSingularView,
                    ConferenceView, ContentSingularView, ContentView,
                    LessonSingularView, LessonView)

app_name = 'lesson'

urlpatterns = [
    path('category/', CategoryView.as_view(), name='category'),
    path('category/c/<str:id>/', CategorySingularView.as_view(), name='single-category'),
    path('lesson/', LessonView.as_view(), name='lesson'),
    path('lesson/l/<str:id>/', LessonSingularView.as_view(), name='single-lesson'),
    path('content/', ContentView.as_view(), name='content'),
    path('content/c/<str:id>/', ContentSingularView.as_view(), name='single-content'),
    path('conference/', ConferenceView.as_view(), name='conference'),
    path('conference/c/<str:id>/', ConferenceSingularView.as_view(), name='single-conference')
]