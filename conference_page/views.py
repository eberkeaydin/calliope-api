# Django Rest Framework  
from rest_framework import (
    generics, 
    status
)
from rest_framework.views import APIView
from rest_framework.response import Response  

# Calliope | ConferencePage
from .models import (
    ConferencePage,
    SurveyQuestion,
    SurveyAnswer
)
from .serializers import (
    ConferencePageSerializer,
    SurveyQuestionSerializer,
    SurveyAnswerSerializer
)


class SurveyView(generics.ListAPIView):

    def get(self, request, *args, **kwargs):
        surveys = SurveyQuestion.objects.all()
        serializers = SurveyQuestionSerializer(surveys, many=True)
        return Response({'status': 'success', "categories":serializers.data}, status=200)


class SurveySingularView(APIView):

    def get(self, request, **kwargs):
        survey = SurveyQuestion.objects.filter(id=kwargs['id'])
        serializer = SurveyQuestionSerializer(survey, many=True)
        return Response(serializer.data)


class SurveyAnswerView(generics.ListAPIView):

    def get(self, request, *args, **kwargs):
        answers = SurveyAnswer.objects.all()
        serializers = SurveyAnswerSerializer(answers, many=True)
        return Response({'status': 'success', "categories":serializers.data}, status=200)


class SurveyAnswerCreateView(generics.CreateAPIView):

    def post(self, request, *args, **kwargs):
        data = request.data.copy()
        survey_answer_object = ConferencePage.objects.create()

        survey_answer_object.id = data['id']
        survey_answer_object.related_survey = data['related_survey']
        survey_answer_object.survey_answer = data['survey_answer'] 
        survey_answer_object.save()

        serializer = SurveyAnswerSerializer(data=data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_204_NO_CONTENT)


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
        conference = ConferencePage.objects.filter(id=kwargs['id'])
        serializer = ConferencePageSerializer(conference, many=True)
        return Response(serializer.data)

# class ConferencePageUpdateView(UpdateAPIView):

#     def put(self, request, *args, **kwargs):
#         data = request.data.copy()
#         conference_page_object = ConferencePage.objects.get(id=data['id'])
#         print(conference_page_object)

#         conference_page_object.id = data['id']
#         conference_page_object.code_editor_url = data['code_editor_url']
#         conference_page_object.directive_text = data['directive_text'] 
#         conference_page_object.save()

#         serializer = ConferencePageSerializer(data=data, partial=True)

#         if serializer.is_valid():
#             serializer.save()
#             return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
#         else:
#             return Response({"status": "success", "data": serializer.data}, status=status.HTTP_204_NO_CONTENT)
