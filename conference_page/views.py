# Django Rest Framework  
from rest_framework import (
    generics, 
    status
)
from rest_framework.views import APIView
from rest_framework.response import Response  
from rest_framework.generics import UpdateAPIView 

# Calliope | ConferencePAge
from .models import ConferencePage
from .serializers import ConferencePageSerializer


class ConferencePageView(generics.ListAPIView):

    def get(self, request, *args, **kwargs):
        result = ConferencePage.objects.all()
        serializers = ConferencePageSerializer(result, many=True)
        return Response({'status': 'success', "categories":serializers.data}, status=200)

    def post(self, request):
        serializer = ConferencePageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class ConferencePageSingularView(APIView):

    def get(self, request, **kwargs):        
        user = ConferencePage.objects.filter(id=kwargs['id'])
        serializer = ConferencePageSerializer(user, many=True)
        return Response(serializer.data)

class ConferencePageUpdateView(UpdateAPIView):

    def put(self, request, *args, **kwargs):
        data = request.data.copy()
        conference_page_object = ConferencePage.objects.get(id=data['id'])
        print(conference_page_object)

        conference_page_object.id = data['id']
        conference_page_object.code_editor_url = data['code_editor_url']
        conference_page_object.directive_text = data['directive_text'] 
        conference_page_object.save()

        serializer = ConferencePageSerializer(data=data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_204_NO_CONTENT)
