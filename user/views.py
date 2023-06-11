# Django Rest Framework  
from rest_framework import generics, request, status, viewsets
from rest_framework.generics import UpdateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

# Calliope | User
from .models import User
from .serializers import UserSerializer


class UserView(generics.ListAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class UserSingularView(APIView):

    def get(self, request, **kwargs):        
        user = User.objects.filter(id=kwargs['id'])
        serializer = UserSerializer(user, many=True)
        return Response(serializer.data)

class UserUpdateView(UpdateAPIView):

    def put(self, request, *args, **kwargs):
        data = request.data.copy()
        user_object = User.objects.get(id=data['id'])

        user_object.id = data['id']
        user_object.user_name = data['user_name']
        user_object.role = data['role']
        user_object.score = data['score'] 
        user_object.save()

        serializer = UserSerializer(data=data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_204_NO_CONTENT)
