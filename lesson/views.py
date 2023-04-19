from django.shortcuts import render  
from rest_framework.views import APIView  
from rest_framework.response import Response  
from rest_framework import status  
from .models import Category, Lesson, Content
from .serializers import CategorySerializer, LessonSerializer, ContentSerializer

import os

from googleapiclient.discovery import build
from datetime import datetime, timedelta

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow

SCOPES = ['https://www.googleapis.com/auth/calendar.events']

  
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

# Video Conferencing
def get_credentials():
    creds = None

    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)

        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    return creds

creds = get_credentials()


def create_google_meet_event(credentials, summary, start_time, end_time, timezone):
    service = build('calendar', 'v3', credentials=credentials)

    event = {
        'summary': summary,
        'start': {
            'dateTime': start_time.isoformat(),
            'timeZone': timezone,
        },
        'end': {
            'dateTime': end_time.isoformat(),
            'timeZone': timezone,
        },
        'conferenceData': {
            'createRequest': {
                'requestId': 'some_unique_id_here',  # Generate a unique ID for the request
            },
        },
    }

    created_event = service.events().insert(calendarId='primary', body=event, conferenceDataVersion=1).execute()

    return created_event

# Replace these values with your actual event details
# event_summary = 'Sample Google Meet Event'
# start_time = datetime.now() + timedelta(hours=1)
# end_time = start_time + timedelta(hours=1)
# timezone = 'America/Los_Angeles'

# created_event = create_google_meet_event(creds, event_summary, start_time, end_time, timezone)

# google_meet_link = created_event['hangoutLink']
# print("Google Meet Link:", google_meet_link)
