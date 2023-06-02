# Django
from django.urls import path

# Calliope | ConferencePage
from .views import (
    ConferencePageView, 
    ConferencePageSingularView, 
    SurveyView, 
    SurveySingularView,
    SurveyAnswerView,
    SurveyAnswerCreateView
)

app_name = 'user'

urlpatterns = [
    path('', ConferencePageView.as_view(), name='conference_page'),
    path('c/<str:id>/', ConferencePageSingularView.as_view(), name='single-conference_page'),
    path('surveys/', SurveyView.as_view(), name='surveys'),
    path('surveys/s/<str:id>/', SurveySingularView.as_view(), name='single-survey'),
    path('surveys/answers/', SurveyAnswerView.as_view(), name='surveys-answers'),
    path('surveys/answers/create/', SurveyAnswerCreateView.as_view(), name='surveys-answers'),
]
