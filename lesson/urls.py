from django.urls import path  
from .views import CategoryView, LessonView, ContentView

app_name = 'lesson'  

urlpatterns = [  
    path('category/', CategoryView.as_view(), name='category'),
    path('lesson/', LessonView.as_view(), name='lesson'),
    path('content/', ContentView.as_view(), name='content')
]  