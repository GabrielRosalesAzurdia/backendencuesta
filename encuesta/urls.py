from django.urls import path , include
from rest_framework import routers
from .views import AnswerViewSet, darResultados

router = routers.DefaultRouter()
router.register(r'answers', AnswerViewSet)

urlpatterns = [
    path('resultados/', darResultados),
    path('', include(router.urls)) ,
]
