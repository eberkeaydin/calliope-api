from django.shortcuts import render  
from rest_framework.views import APIView  
from rest_framework.response import Response  
from rest_framework import status  
from .models import Category, Lesson, Content
from .serializers import CategorySerializer, LessonSerializer, ContentSerializer
  
class CategoryView(APIView):  
  
    def get(self, request, *args, **kwargs):  
        result = Category.objects.all()  
        serializers = CategorySerializer(result, many=True)  
        return Response({'status': 'success', "categories":serializers.data}, status=200)  
  
    def post(self, request):  
        serializer = CategorySerializer(data=request.data)  
        if serializer.is_valid():  
            serializer.save()  
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)  
        else:  
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST) 
        
class LessonView(APIView):  
  
    def get(self, request, *args, **kwargs):  
        result = Lesson.objects.all()  
        serializers = LessonSerializer(result, many=True)  
        return Response({'status': 'success', "lessons":serializers.data}, status=200)  
  
    def post(self, request):  
        serializer = LessonSerializer(data=request.data)  
        if serializer.is_valid():  
            serializer.save()  
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)  
        else:  
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST) 
        
class ContentView(APIView):  
  
    def get(self, request, *args, **kwargs):  
        result = Content.objects.all()  
        serializers = ContentSerializer(result, many=True)  
        return Response({'status': 'success', "contents":serializers.data}, status=200)  
  
    def post(self, request):  
        serializer = ContentSerializer(data=request.data)  
        if serializer.is_valid():  
            serializer.save()  
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)  
        else:  
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST) 