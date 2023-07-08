from rest_framework import viewsets
from .serializer import AnswerSerializer
from .models import Answer
from django.views.decorators.csrf import csrf_exempt

class AnswerViewSet(viewsets.ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer