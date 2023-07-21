from rest_framework import viewsets
from .serializer import AnswerSerializer
from .models import Answer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
import json

class AnswerViewSet(viewsets.ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer

@csrf_exempt
@api_view(['GET'])
def darResultados(request):
    queryset = Answer.objects.all()
    respuestas = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
    # for question in queryset:
    #     i = 1
    #     while i<=15:
    #         actual = question.getQuestion(i)
    #         if (actual == 0):
    #             respuestas[i-1][0] = respuestas[i-1][0] + 1
    #         if(actual == 1):
    #             respuestas[i-1][1] = respuestas[i-1][1] + 1
    #         if(actual == 2):
    #             respuestas[i-1][2] = respuestas[i-1][2] + 1
    data = {'content':json.dumps(respuestas)}
    return Response(data)
        