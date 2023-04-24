# Django Rest Framework  
from rest_framework import generics
from rest_framework import status
from rest_framework.views import APIView  
from rest_framework.response import Response  

# Calliope | User
from .models import User
from .serializers import UserSerializer


class UserView(generics.ListAPIView):  

    def get(self, request, *args, **kwargs):  
        result = User.objects.all()  
        serializers = UserSerializer(result, many=True)  
        return Response({'status': 'success', "categories":serializers.data}, status=200)  

    def post(self, request):  
        serializer = UserSerializer(data=request.data)  
        if serializer.is_valid():  
            serializer.save()  
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)  
        else:  
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class UserSingularView(APIView):

    def get(self, request, **kwargs):
        user = User.objects.filter(id=kwargs['id'])
        serializer = UserSerializer(user, many=True)
        return Response(serializer.data)

    def update(self, request, role, score):
        data = request.data.copy()
        data['role'] = role
        data['score'] = score

        serializer = UserSerializer(data=data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)  
        else:  
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
