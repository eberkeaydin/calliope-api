# Django
from django.urls import path

# Calliope | ConferencePage
from .views import ConferencePageView, ConferencePageSingularView, ConferencePageUpdateView

app_name = 'user'

urlpatterns = [
    path('', ConferencePageView.as_view(), name='conference_page'),
    path('c/<str:id>/', ConferencePageSingularView.as_view(), name='single-conference_page'),
    path('update/', ConferencePageUpdateView.as_view(), name='conference_page-update'),
]
