# Django
from django.urls import path

# Calliope | Quiz
from .views import UserView, UserSingularView

app_name = 'user'

urlpatterns = [
    path('', UserView.as_view(), name='user'),
    path('u/<str:id>/', UserSingularView.as_view(), name='single-user'),
]
