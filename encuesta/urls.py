from django.urls import path , include
from rest_framework import routers
from .views import AnswerViewSet, darResultados

router = routers.DefaultRouter()
router.register(r'answers', AnswerViewSet)

urlpatterns = [
    path('', include(router.urls)) ,
    path('resultados/', darResultados),
]
