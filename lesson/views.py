# Python
import os
from datetime import datetime, timedelta

# Django Rest Framework  
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics

# Google
import google
from googleapiclient.discovery import build
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow

# Calliope | Lesson
from .models import Category, Lesson, Conference, Content
from .serializers import CategorySerializer, LessonSerializer, ConferenceSerializer, ContentSerializer

SCOPES = ['https://www.googleapis.com/auth/calendar.events']


class CategoryView(generics.ListAPIView):

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


class CategorySingularView(APIView):

    def get(self, request, **kwargs):        
        category = Category.objects.filter(id=kwargs['id'])
        serializer = CategorySerializer(category, many=True)
        return Response(serializer.data)


class LessonView(generics.ListAPIView):

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


class LessonSingularView(APIView):

    def get(self, request, **kwargs):        
        category = Lesson.objects.filter(id=kwargs['id'])
        serializer = LessonSerializer(category, many=True)
        return Response(serializer.data)


class ContentView(generics.ListAPIView):

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


class ContentSingularView(APIView):

    def get(self, request, **kwargs):        
        category = Content.objects.filter(id=kwargs['id'])
        serializer = ContentSerializer(category, many=True)
        return Response(serializer.data)


class ConferenceView(APIView):

    def get(self, request, *args, **kwargs):
        result = Conference.objects.all()
        serializers = ConferenceSerializer(result, many=True)
        return Response({'status': 'success', "contents":serializers.data,}, status=200)

    def post(self, request):
        creds = self.get_credentials()
        event_summary = request.data['conference_topic']
        start_time = datetime.now() + timedelta(hours=1)
        end_time = start_time + timedelta(minutes=30)
        meet_timezone = 'Europe/Istanbul'

        created_event = self.create_google_meet_event(creds, event_summary, start_time, end_time, meet_timezone)

        google_meet_link = created_event['hangoutLink']
        print("Google Meet Link:", google_meet_link)

        data = request.data.copy()
        data['conference_url'] = google_meet_link

        serializer = ConferenceSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:  
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def get_credentials(self):
        creds = None

        if os.path.exists('token.json'):
            creds = Credentials.from_authorized_user_file('token.json', SCOPES)

        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                try:
                    creds.refresh(Request())
                except google.auth.exceptions.RefreshError as e:
                    # Handle token refresh error and reauthorize
                    flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
                    creds = flow.run_local_server(port=0)
            else:
                flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
                creds = flow.run_local_server(port=0)

            with open('token.json', 'w') as token:
                token.write(creds.to_json())

        return creds

    
    def create_google_meet_event(self, credentials, summary, start_time, end_time, meet_timezone):
        service = build('calendar', 'v3', credentials=credentials)

        event = {
            'summary': summary,
            'start': {
                'dateTime': start_time.isoformat(),
                'timeZone': meet_timezone,
            },
            'end': {
                'dateTime': end_time.isoformat(),
                'timeZone': meet_timezone,
            },
            'conferenceData': {
                'createRequest': {
                    'requestId': 'some_unique_id_here',  # Generate a unique ID for the request
                },
            },
        }
        created_event = service.events().insert(calendarId='primary', body=event, conferenceDataVersion=1).execute()

        return created_event


class ConferenceSingularView(APIView):

    def get(self, request, **kwargs):        
        category = Conference.objects.filter(id=kwargs['id'])
        serializer = ConferenceSerializer(category, many=True)
        return Response(serializer.data)